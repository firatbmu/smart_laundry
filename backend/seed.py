"""
Veritabanına başlangıç makinelerini ekler.
Sadece bir kez çalıştır: python seed.py
"""
from database import engine, Base, SessionLocal
from models import Machine

Base.metadata.create_all(bind=engine)

MACHINES = [
    Machine(name="Makine 1", esp_device_id="esp32_smart_laundry_001", status="AVAILABLE"),
]

db = SessionLocal()
try:
    for m in MACHINES:
        exists = db.query(Machine).filter(Machine.esp_device_id == m.esp_device_id).first()
        if not exists:
            db.add(m)
    db.commit()
    print("Baslangic makineleri eklendi.")
except Exception as e:
    db.rollback()
    print(f"Hata: {e}")
finally:
    db.close()
