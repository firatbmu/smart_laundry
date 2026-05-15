"""
Arka planda çalışan SMS bildirim servisi.
Her POLL_INTERVAL saniyede bir sıra pozisyonlarını kontrol eder,
eşiğe (SMS_NOTIFY_THRESHOLD) ulaşan kullanıcılara SMS gönderir.
"""
import logging
import threading
import time

from services.sms import SMS_NOTIFY_THRESHOLD, send_queue_notification

logger = logging.getLogger(__name__)

POLL_INTERVAL = 10  # saniye


def _check_and_notify():
    """Tüm WAITING kayıtları tara, eşiğe gelenlere SMS gönder."""
    from database import SessionLocal
    from models import Queue, User

    db = SessionLocal()
    try:
        waiting_entries = (
            db.query(Queue)
            .filter(Queue.status == "WAITING", Queue.sms_sent == False)  # noqa: E712
            .all()
        )

        for entry in waiting_entries:
            # Bu makine için kaçıncı sırada?
            position = (
                db.query(Queue)
                .filter(
                    Queue.machine_id == entry.machine_id,
                    Queue.status == "WAITING",
                    Queue.created_at <= entry.created_at,
                )
                .count()
            )

            if position <= SMS_NOTIFY_THRESHOLD:
                # Kullanıcının telefon numarasını bul
                user = db.query(User).filter(User.tc == entry.student_id).first()
                if not user:
                    continue

                # Telefon numarasını uluslararası formata çevir
                telefon = user.telefon.strip()
                if telefon.startswith("0"):
                    telefon = "+9" + telefon  # 05XX → +905XX

                machine_name = entry.machine.name if entry.machine else f"Machine {entry.machine_id}"

                logger.info(
                    f"SMS bildirimi: {user.ad} {user.soyad} → "
                    f"{machine_name} sırası #{position}"
                )

                success = send_queue_notification(telefon, machine_name, position)
                if success:
                    entry.sms_sent = True
                    db.commit()

    except Exception as e:
        logger.error(f"Notifier hatası: {e}")
    finally:
        db.close()


def _notifier_loop():
    """Arka planda sürekli çalışan döngü."""
    logger.info(
        f"SMS notifier başlatıldı — her {POLL_INTERVAL}s kontrol, "
        f"eşik: pozisyon ≤ {SMS_NOTIFY_THRESHOLD}"
    )
    while True:
        try:
            _check_and_notify()
        except Exception as e:
            logger.error(f"Notifier loop hatası: {e}")
        time.sleep(POLL_INTERVAL)


def start_queue_notifier():
    """Notifier thread'ini daemon olarak başlat."""
    thread = threading.Thread(target=_notifier_loop, daemon=True, name="queue-notifier")
    thread.start()
    return thread
