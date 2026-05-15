import logging
import os
from pathlib import Path

from dotenv import load_dotenv

# sms.py → backend/services/sms.py  ·  .env → backend/.env
_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

logger = logging.getLogger(__name__)

SMS_NOTIFY_THRESHOLD = int(os.getenv("SMS_NOTIFY_THRESHOLD", "2"))


def _get_credentials():
    """Her çağrıda .env'den güncel credentials oku (explicit path ile)."""
    load_dotenv(dotenv_path=_ENV_PATH, override=True)
    return {
        "sid": os.getenv("TWILIO_ACCOUNT_SID", "").strip(),
        "token": os.getenv("TWILIO_AUTH_TOKEN", "").strip(),
        "from": os.getenv("TWILIO_FROM_NUMBER", "").split("#")[0].strip(),
    }


def send_sms(to_number: str, message: str) -> bool:
    """Twilio ile SMS gönder. Başarıda True, hata durumunda False döner."""
    creds = _get_credentials()

    if not all([creds["sid"], creds["token"], creds["from"]]):
        logger.warning("Twilio credentials eksik — .env dosyasını kontrol edin.")
        return False

    if creds["sid"].startswith("BURAYA"):
        logger.warning("Twilio credentials henüz ayarlanmamış — .env doldurun.")
        return False

    try:
        from twilio.rest import Client
        client = Client(creds["sid"], creds["token"])
        msg = client.messages.create(
            body=message,
            from_=creds["from"],
            to=to_number,
        )
        logger.info(f"SMS gönderildi → {to_number} | SID: {msg.sid}")
        return True
    except Exception as e:
        logger.error(f"SMS gönderme hatası → {to_number}: {e}")
        return False


def send_queue_notification(to_number: str, machine_name: str, position: int) -> bool:
    """Sıra bildirimi SMS'i gönder."""
    message = (
        f"Smart Laundry: Your queue position for {machine_name} "
        f"is now #{position}. Please get ready!"
    )
    return send_sms(to_number, message)
