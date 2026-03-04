# AI Kullanim Rehberi - Kisi 1 (IoT/Hardware & Takim Lideri)

Bu rehber, yapay zeka asistani kullanarak gorevlerini tamamlamani saglayacak.

---

## Temel Kullanim Kurallari

1. **Gorevi AI'a yapistir**
2. **"Adim adim anlat" de**
3. **Kodu al, calistir**
4. **Hata varsa hatayi yapistir**
5. **Calisana kadar tekrarla**

---

# HAFTA 1: Proje Kurulumu

## Gorev 1.1: GitHub Repository Olusturma

### Prompt:
```
GitHub'da yeni bir repository nasil olusturulur?
Repository adi: smart-laundry
Aciklama: Akilli camasirhane takip sistemi
Public olsun
README.md otomatik olusturulsun
Adim adim anlat, ekran goruntuleri olmadan metin olarak.
```

### Beklenen Cikti:
- github.com/kullanici/smart-laundry adresi

---

## Gorev 1.2: Takim Uyelerini Ekleme

### Prompt:
```
GitHub repository'ye collaborator (takim uyesi) nasil eklenir?
5 kisilik bir takim var.
Hepsine write yetkisi verilecek.
Adim adim anlat.
```

---

## Gorev 1.3: Proje Klasor Yapisi

### Prompt:
```
Python projesi icin klasor yapisi olustur.
Proje adi: smart-laundry
Icerik:
- backend/ (Flask API)
- mobile/ (Kivy uygulama)
- hardware/ (ESP32 kodlari)
- tests/ (test dosyalari)
- docs/ (dokumantasyon)

Her klasorde __init__.py ve README.md olsun.
Bana terminal komutlarini ver (Windows icin).
```

---

# HAFTA 2: ESP32 ve MicroPython Kurulumu

## Gorev 2.1: MicroPython Yukleme

### Prompt:
```
ESP32'ye MicroPython nasil yuklenir?
Isletim sistemi: Windows
Adimlar:
1. Firmware indirme
2. esptool kurulumu
3. Flash islemi
Tum komutlari ve linkleri ver.
```

### Olasi Hata ve Cozum:
```
Hata: "COM port bulunamadi" veya "Access denied"

Bu hatayi aliyorum, nasil cozerim?
ESP32 Windows'ta COM portunda gorunmuyor.
```

---

## Gorev 2.2: Thonny IDE Kurulumu

### Prompt:
```
Thonny IDE'yi Windows'a nasil kurarim?
ESP32 ile nasil baglarim?
MicroPython interpreter nasil secilir?
Adim adim anlat.
```

---

## Gorev 2.3: LED Test Kodu

### Prompt:
```
MicroPython ile ESP32'de dahili LED'i yak/sondur.
GPIO2 pini kullan.
1 saniye aralikla yanip sonsun.
Kodu yaz ve acikla.
```

### Beklenen Kod:
```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(1)  # LED yak
    sleep(1)
    led.value(0)  # LED sondur
    sleep(1)
```

---

## Gorev 2.4: WiFi Baglantisi

### Prompt:
```
MicroPython ile ESP32'yi WiFi'ye bagla.
SSID: "YurtWiFi"
Sifre: "12345678"
Baglanti durumunu yazdir.
IP adresini goster.
```

### Olasi Hata:
```
Hata: "OSError: Wifi Internal Error"

WiFi'ye baglanamiyorum, bu hatayi aliyorum.
ESP32 MicroPython kullaniyorum.
```

---

# HAFTA 3: ADXL345 Sensor Entegrasyonu

## ADXL345 Nedir?
ADXL345, 3 eksenli dijital ivme olcer (accelerometer) sensorudur.
- Titresim, hareket ve egim algilayabilir
- I2C veya SPI ile iletisim kurar
- Bu projede camasir makinesinin titresimini olcmek icin kullanacagiz

## Gorev 3.1: I2C Baglanti Kontrolu

### Prompt:
```
MicroPython ile ESP32'de I2C taramasi yap.
SDA: GPIO21
SCL: GPIO22
Bagli cihazlarin adreslerini listele.
ADXL345 adresi 0x53 olmali.
```

### Beklenen Kod:
```python
from machine import I2C, Pin

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
devices = i2c.scan()

print("Bulunan cihazlar:")
for d in devices:
    print(f"  Adres: {hex(d)}")
```

### Beklenen Cikti:
```
Bulunan cihazlar:
  Adres: 0x53    <- ADXL345
```

---

## Gorev 3.2: ADXL345 Veri Okuma

### Prompt:
```
MicroPython ile ADXL345 sensorunden veri oku.
ESP32 kullaniyorum.
I2C baglantisi: SDA=21, SCL=22
Ivme (ax, ay, az) verilerini oku.
Her 500ms'de bir ekrana yazdir.
Harici kutuphane kullanmadan, register'lardan direkt oku.
NOT: ADXL345 sadece ivme olcer, gyro yok.
```

### ADXL345 Baglanti Semasi:
```
ADXL345         ESP32
--------        --------
VCC      ->     3.3V
GND      ->     GND
SDA      ->     GPIO21
SCL      ->     GPIO22
```

### Olasi Hata:
```
Hata: "OSError: [Errno 110] ETIMEDOUT"

I2C uzerinden ADXL345'den veri okuyamiyorum.
Baglanti semam:
- VCC -> 3.3V
- GND -> GND
- SDA -> GPIO21
- SCL -> GPIO22
```

### Cozum:
```
1. Baglantilari kontrol et (ozellikle GND)
2. 3.3V kullandigindan emin ol (5V KULLANMA!)
3. I2C scan ile adres gorunuyor mu kontrol et
4. Kablolari kisa tut (uzun kablo parazit yapar)
```

---

## Gorev 3.3: sensor.py Modulu

### Prompt:
```
MicroPython icin ADXL345 sensor sinifi yaz.
Dosya adi: sensor.py
Ozellikler:
- __init__ ile I2C baslat ve sensoru yapilandir
- read_accel() -> (ax, ay, az) tuple dondur (g cinsinden)
- read_raw() -> (raw_x, raw_y, raw_z) ham degerler
- calibrate() -> sensor kalibrasyonu
NOT: ADXL345'te gyro yok, sadece ivme olcer.
Temiz, okunabilir kod yaz.
```

---

# HAFTA 4: MQTT Iletisimi

## Gorev 4.1: MQTT Temelleri

### Prompt:
```
MQTT nedir? Nasil calisir?
Publisher, Subscriber, Broker kavramlarini acikla.
Topic yapisi nasil olmali?
IoT projeleri icin neden kullanilir?
Basit ve anlasilir sekilde anlat.
```

---

## Gorev 4.2: umqtt Kurulumu

### Prompt:
```
MicroPython'da umqtt.simple kutuphanesi nasil kurulur?
ESP32 kullaniyorum.
Thonny IDE ile yukleme adimlarini anlat.
```

---

## Gorev 4.3: MQTT Client Kodu

### Prompt:
```
MicroPython ile MQTT client yaz.
ESP32 kullaniyorum.
Broker: test.mosquitto.org (ucretsiz test broker)
Port: 1883
Topic: laundry/machine/001
JSON formatinda mesaj gonder:
{
  "device_id": "esp32_001",
  "vibration": 2.45,
  "status": "RUNNING",
  "timestamp": "2024-01-15 14:30:00"
}
Her 5 saniyede bir gondersin.
```

### Olasi Hata:
```
Hata: "MQTTException: 5" veya "Connection refused"

MQTT broker'a baglanamiyorum.
test.mosquitto.org kullaniyorum.
ESP32 WiFi'ye bagli, internet var.
```

---

## Gorev 4.4: Backend ile Test

### Prompt:
```
ESP32'den MQTT ile gonderdigim mesajlari 
bilgisayarimda nasil gorebilirim?
Windows kullaniyorum.
mosquitto_sub komutu veya Python ile dinleme kodu ver.
Topic: laundry/machine/#
```

---

# HAFTA 5: Titresim Algoritmasi

## Gorev 5.1: Titresim Hesaplama

### Prompt:
```
ADXL345 ivme verilerinden titresim siddeti hesapla.
Formul: magnitude = sqrt(ax^2 + ay^2 + az^2)
MicroPython kodu yaz.
Yercekim etkisini cikar (yaklasik 1g).
Sonuc g biriminde olsun.
```

### Aciklama:
```
Titresim = Ivme degisimi
- Makine duruyor: ax, ay, az degerleri sabit (sadece yercekimi)
- Makine calisiyor: ax, ay, az degerleri surekli degisiyor (titresim)
- magnitude hesaplayarak tek bir sayi elde ediyoruz
```

---

## Gorev 5.2: Durum Tespiti Algoritmasi

### Prompt:
```
Titresim degerine gore makine durumu tespit et.
MicroPython kodu yaz.
Kurallar:
- vibration > 1.5 -> "RUNNING" (makine calisiyor)
- vibration < 0.5 -> "AVAILABLE" (makine bos)
- arada -> "FINISHING" (bitiyor olabilir)

Son 5 olcumun ortalamasini al (gurultu filtresi).
Durum degisince MQTT ile bildir.
```

---

## Gorev 5.3: main.py Ana Dongusu

### Prompt:
```
ESP32 icin ana program yaz (main.py).
MicroPython kullaniyorum.
Islevler:
1. WiFi'ye baglan
2. MQTT broker'a baglan
3. Sensor'u baslat
4. Sonsuz dongude:
   - Titresim oku
   - Durum hesapla
   - 5 saniyede bir MQTT'ye gonder
   - Hata olursa yeniden baglan
Temiz, modular kod yaz.
```

---

# HAFTA 6: Coklu Cihaz Destegi

## Gorev 6.1: Config Dosyasi

### Prompt:
```
ESP32 icin JSON config dosyasi olustur.
Dosya: config.json
Icerik:
- device_id
- wifi_ssid
- wifi_password
- mqtt_broker
- mqtt_port
- mqtt_topic
- threshold degerleri

MicroPython ile bu dosyayi okuma kodunu yaz.
```

---

## Gorev 6.2: Farkli Device ID'ler

### Prompt:
```
3 farkli ESP32 icin ayri config dosyalari olustur.
Device ID'ler: esp32_001, esp32_002, esp32_003
Her biri farkli topic'e gondersin:
- laundry/machine/001
- laundry/machine/002
- laundry/machine/003
```

---

## Gorev 6.3: Hata Yonetimi

### Prompt:
```
MicroPython'da WiFi ve MQTT hata yonetimi ekle.
Senaryolar:
1. WiFi baglantisi koparsa -> yeniden baglan
2. MQTT baglantisi koparsa -> yeniden baglan
3. Sensor okunamasa -> hata logla, devam et
try/except kullan.
Reconnect mantigi ekle (5 saniye bekle, tekrar dene).
```

---

# HAFTA 7: Optimizasyon

## Gorev 7.1: Exception Handling

### Prompt:
```
MicroPython koduma kapsamli hata yonetimi ekle.
Mevcut kodum: [kodunu yapistir]
Eklenecekler:
- try/except bloklari
- Hata loglama (dosyaya yazma)
- Graceful degradation (bir sey bozulsa bile devam)
```

---

## Gorev 7.2: WiFi Reconnect

### Prompt:
```
MicroPython'da otomatik WiFi yeniden baglama yaz.
Ozellikler:
- Baglanti kontrolu (is_connected)
- Kopunca 5 kez dene
- Her denemede 3 saniye bekle
- Basarisiz olursa soft reset
```

---

## Gorev 7.3: LED Durum Gostergesi

### Prompt:
```
ESP32 dahili LED ile sistem durumunu goster.
MicroPython kodu yaz.
- Hizli yanip sonme: WiFi'ye baglaniliyor
- Yavas yanip sonme: MQTT'ye baglaniliyor
- Surekli yanik: Her sey calisiyor
- Surekli sonuk: Hata var
```

---

# HAFTA 8: Demo Hazirligi

## Gorev 8.1: Demo Senaryosu

### Prompt:
```
Camasirhane takip sistemi icin demo senaryosu yaz.
3 dakikalik sunum.
Gosterilecekler:
1. Makine kapaliyken durum (AVAILABLE)
2. Makine calisirken durum (RUNNING)
3. Mobil uygulamada canli guncelleme
4. Sira sistemi (opsiyonel)
Senaryo adimlarini yaz.
```

---

## Gorev 8.2: Baglanti Semasi Dokumantasyonu

### Prompt:
```
ADXL345 - ESP32 baglanti semasini Markdown formatinda yaz.
Tablo olarak goster.
ASCII diagram ekle.
README.md'ye eklenecek formatta.
```

### Beklenen Cikti:
```
| ADXL345 Pin | ESP32 Pin | Aciklama |
|-------------|-----------|----------|
| VCC         | 3.3V      | Guc (5V KULLANMA!) |
| GND         | GND       | Toprak |
| SDA         | GPIO21    | I2C Veri |
| SCL         | GPIO22    | I2C Saat |

     ADXL345              ESP32
    +-------+           +-------+
    | VCC   |---[3.3V]--| 3V3   |
    | GND   |---[GND]---| GND   |
    | SDA   |---[I2C]---| GPIO21|
    | SCL   |---[I2C]---| GPIO22|
    +-------+           +-------+
```

---

# SIK KARSILASILAN HATALAR

## Hata 1: COM Port Bulunamadi
```
Prompt: "Windows'ta ESP32 COM portu gorunmuyor. 
Aygit Yoneticisi'nde 'Diger cihazlar' altinda sari unlem var.
CP210x veya CH340 driver mi yuklemem lazim?"
```

## Hata 2: MicroPython Import Hatasi
```
Prompt: "MicroPython'da 'ImportError: no module named umqtt' hatasi aliyorum.
Kutuphaneyi nasil yuklerim? Thonny kullaniyorum."
```

## Hata 3: I2C Timeout
```
Prompt: "ADXL345 I2C timeout hatasi veriyor.
Baglanti dogru, voltaj 3.3V.
Pull-up resistor gerekli mi?
I2C adresi 0x53 olmali."
```

### Cozum Adimlari:
```
1. I2C scan yap - adres gorunuyor mu?
2. Kablo baglantilarini kontrol et
3. 3.3V kullandigindan emin ol
4. Bazi ADXL345 modullerinde yerlesik pull-up var
5. Yoksa 4.7K pull-up ekle (SDA ve SCL'ye)
```

## Hata 4: MQTT Baglanti Reddedildi
```
Prompt: "MQTT broker'a baglanamiyorum.
Hata: Connection refused.
Broker: test.mosquitto.org
Firewall mi engelliyor? Nasil test ederim?"
```

---

# YARDIM ISTEME SABLONU

Takildiginda su formati kullan:

```
SORUN: [Ne yapmaya calisiyorsun]
HATA: [Tam hata mesaji]
DENEDIKLERIM: [Simdiye kadar ne denedin]
ORTAM: ESP32, MicroPython, Windows
KOD: [Ilgili kod parcasi]
```

---

**Basarilar!**
