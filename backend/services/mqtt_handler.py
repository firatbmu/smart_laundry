import json
import logging
import threading
from datetime import datetime

import paho.mqtt.client as mqtt

from database import SessionLocal
from models import Machine, Queue
from services.analysis import detect_status

logger = logging.getLogger(__name__)

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "laundry/machine/#"
HISTORY_SIZE = 5  # Gürültü filtresi: son kaç ölçümün ortalaması alınsın

# Her cihaz için ayrı titreşim geçmişi
_vibration_history: dict[str, list[float]] = {}


# ── paho-mqtt v2 callback imzaları ──────────────────────────────────────────

def _on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.subscribe(TOPIC)
        logger.info("MQTT broker'a bağlandı, topic dinleniyor: %s", TOPIC)
    else:
        logger.error("MQTT bağlantı hatası, reason_code=%s", reason_code)


def _on_disconnect(client, userdata, flags, reason_code, properties):
    if reason_code != 0:
        logger.warning("MQTT bağlantısı beklenmedik şekilde kesildi (reason=%s)", reason_code)


def _on_message(client, userdata, msg):
    try:
        payload: dict = json.loads(msg.payload.decode())
    except (json.JSONDecodeError, UnicodeDecodeError):
        logger.error("JSON parse hatası | payload=%r", msg.payload)
        return

    device_id: str | None = payload.get("device_id")
    vibration: float | None = payload.get("vibration")

    if not device_id:
        logger.warning("device_id eksik, mesaj atlandı | payload=%s", payload)
        return

    # Titreşim geçmişini güncelle ve durum hesapla
    history = _vibration_history.setdefault(device_id, [])
    if vibration is not None:
        history.append(float(vibration))
        if len(history) > HISTORY_SIZE:
            history.pop(0)
    status = detect_status(history)

    db = SessionLocal()
    try:
        machine: Machine | None = (
            db.query(Machine).filter(Machine.esp_device_id == device_id).first()
        )
        if machine is None:
            logger.warning("Bilinmeyen device_id: %s", device_id)
            return

        old_status = machine.status
        machine.status = status
        machine.last_update = datetime.utcnow()
        db.commit()

        logger.info("%s | %s → %s", machine.name, old_status, status)

        # Makine yeni boşaldıysa sıradaki kişiye bildir
        if status == "AVAILABLE" and old_status != "AVAILABLE":
            _notify_next_in_queue(db, machine.id)

    except Exception:
        db.rollback()
        logger.exception("DB güncelleme hatası (device_id=%s)", device_id)
    finally:
        db.close()


def _notify_next_in_queue(db, machine_id: int) -> None:
    """Sıradaki WAITING kaydını NOTIFIED yap."""
    next_entry: Queue | None = (
        db.query(Queue)
        .filter(Queue.machine_id == machine_id, Queue.status == "WAITING")
        .order_by(Queue.created_at)
        .first()
    )
    if next_entry:
        next_entry.status = "NOTIFIED"
        db.commit()
        logger.info(
            "Sıra bildirimi: öğrenci=%s, makine_id=%s",
            next_entry.student_id,
            machine_id,
        )


# ── Public API ───────────────────────────────────────────────────────────────

def start_mqtt_listener() -> None:
    """MQTT listener'ı arka planda daemon thread olarak başlat."""

    def _run():
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.on_connect = _on_connect
        client.on_disconnect = _on_disconnect
        client.on_message = _on_message
        try:
            client.connect(BROKER, PORT, keepalive=60)
            client.loop_forever(retry_first_connection=True)
        except Exception:
            logger.exception("MQTT başlatma hatası")

    thread = threading.Thread(target=_run, daemon=True, name="mqtt-listener")
    thread.start()
    logger.info("MQTT listener thread başlatıldı")
