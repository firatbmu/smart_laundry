# main.py - LED Durum Gostergesi ile Final Versiyon

import network
import time
import math
import ujson
import machine
from machine import Pin, I2C
from sensor import ADXL345
from umqtt.simple import MQTTClient

# =============================================
# --- AYARLAR ---
# =============================================
WIFI_SSID           = "Burak"
WIFI_PASSWORD       = "123456789."
MQTT_BROKER         = "broker.hivemq.com"
MQTT_PORT           = 1883
CLIENT_ID           = "esp32_smart_laundry_001"
MQTT_TOPIC          = "laundry/machine/001"
THRESHOLD_RUNNING   = 0.150
THRESHOLD_AVAILABLE = 0.150
MAX_RETRY           = 5
RETRY_DELAY         = 3
MAX_SENSOR_ERRORS   = 10

# =============================================
# --- LED YONETIMI ---
# =============================================

# ESP32 dahili LED GPIO2'de
led = Pin(2, Pin.OUT)

def led_fast_blink(duration=5):
    """Hizli yanip sonme: WiFi'ye baglaniliyor."""
    end_time = time.time() + duration
    while time.time() < end_time:
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)

def led_slow_blink(duration=3):
    """Yavas yanip sonme: MQTT'ye baglaniliyor."""
    end_time = time.time() + duration
    while time.time() < end_time:
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)

def led_on():
    """Surekli yanik: Her sey calisiyor."""
    led.value(1)

def led_off():
    """Surekli sonuk: Kritik hata."""
    led.value(0)

# =============================================
# --- HATA LOGLAMA ---
# =============================================

def log_error(message):
    timestamp = time.time()
    log_line = f"[{timestamp}] HATA: {message}\n"
    print(log_line.strip())
    try:
        with open("error.log", "a") as f:
            f.write(log_line)
    except:
        pass

# =============================================
# --- WIFI YONETIMI ---
# =============================================

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        return wlan

    for attempt in range(1, MAX_RETRY + 1):
        print(f"WiFi baglanti denemesi {attempt}/{MAX_RETRY}...")
        # LED hizli yanip sonsun (WiFi aranıyor sinyali)
        led_fast_blink(duration=2)
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1

        if wlan.isconnected():
            print(f"WiFi OK! IP: {wlan.ifconfig()[0]}")
            return wlan

        print(f"Deneme {attempt} basarisiz. {RETRY_DELAY} saniye bekleniyor...")
        wlan.disconnect()
        time.sleep(RETRY_DELAY)

    led_off()  # Hata: LED sonsun
    log_error(f"WiFi baglanamadi. Yeniden baslatiliyor.")
    time.sleep(3)
    machine.soft_reset()

def check_wifi(wlan):
    if not wlan.isconnected():
        print("WiFi koptu! Yeniden baglaniliyor...")
        log_error("WiFi baglantisi koptu.")
        return connect_wifi()
    return wlan

# =============================================
# --- MQTT YONETIMI ---
# =============================================

def connect_mqtt():
    for attempt in range(1, MAX_RETRY + 1):
        print(f"MQTT baglanti denemesi {attempt}/{MAX_RETRY}...")
        # LED yavas yanip sonsun (MQTT aranıyor sinyali)
        led_slow_blink(duration=2)
        try:
            client = MQTTClient(CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
            client.connect()
            print(f"MQTT OK! Broker: {MQTT_BROKER}")
            return client
        except OSError as e:
            log_error(f"MQTT hatasi (deneme {attempt}): {e}")
            time.sleep(RETRY_DELAY)

    led_off()  # Hata: LED sonsun
    log_error("MQTT baglanamadi. Yeniden baslatiliyor.")
    time.sleep(3)
    machine.soft_reset()

# =============================================
# --- SENSOR VE HESAPLAMA ---
# =============================================

def calculate_vibration(ax, ay, az):
    magnitude = math.sqrt(ax**2 + ay**2 + az**2)
    return abs(magnitude - 1.0)

def get_status(vibration):
    if vibration > THRESHOLD_RUNNING:
        return "RUNNING"
    else:
        return "AVAILABLE"

def safe_read_sensor(sensor):
    try:
        return sensor.read_accel()
    except OSError as e:
        log_error(f"Sensor okuma hatasi: {e}")
        return None

# =============================================
# --- ANA PROGRAM ---
# =============================================

print("=" * 40)
print("Akilli Camasirhane Sistemi Basliyor...")
print("=" * 40)

wlan = connect_wifi()

try:
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    sensor = ADXL345(i2c)
    print("Sensor OK!")
except Exception as e:
    led_off()
    log_error(f"Sensor baslatma hatasi: {e}")
    time.sleep(5)
    machine.soft_reset()

mqtt_client = connect_mqtt()

# Her sey hazir: LED surekli yaksın
led_on()

vibration_history = []
last_status = ""
error_count = 0

print("\nSistem hazir! Olcumler basliyor...\n")

while True:
    try:
        wlan = check_wifi(wlan)

        accel_data = safe_read_sensor(sensor)

        if accel_data is None:
            error_count += 1
            print(f"Sensor atlandi. (Hata: {error_count}/{MAX_SENSOR_ERRORS})")
            if error_count >= MAX_SENSOR_ERRORS:
                led_off()
                log_error("Cok fazla sensor hatasi. Yeniden baslatiliyor.")
                machine.soft_reset()
            time.sleep(2)
            continue

        error_count = 0
        ax, ay, az = accel_data

        vibration = calculate_vibration(ax, ay, az)
        vibration_history.append(vibration)
        if len(vibration_history) > 10:
            vibration_history.pop(0)

        avg_vibration = sum(vibration_history) / len(vibration_history)
        current_status = get_status(avg_vibration)

        # Surekli yanik: sistem calisiyor
        led_on()

        print(f"Titresim: {avg_vibration:.3f}g | Durum: {current_status}")

        try:
            message = ujson.dumps({
                "device_id": CLIENT_ID,
                "vibration": round(avg_vibration, 3),
                "status": current_status,
                "timestamp": time.time()
            })
            mqtt_client.publish(MQTT_TOPIC.encode(), message.encode())
        except OSError as e:
            log_error(f"MQTT gonderim hatasi: {e}")
            mqtt_client = connect_mqtt()
            led_on()  # MQTT yeniden baglandi, LED tekrar yaksın

        if current_status != last_status:
            print(f">>> DURUM DEGISTI: {last_status} -> {current_status}")
            last_status = current_status

        time.sleep(5)

    except Exception as e:
        log_error(f"Beklenmedik hata: {e}")
        time.sleep(5)