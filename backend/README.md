# Backend — Smart Laundry

FastAPI + SQLite + MQTT tabanlı REST API. Çamaşır makinelerinin durumunu yönetir, ESP32 sensör verilerini işler ve sıra sistemini çalıştırır.

---

## Kurulum

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install fastapi uvicorn sqlalchemy paho-mqtt pandas pytest httpx
```

---

## Çalıştırma

```bash
# 1. Başlangıç makinelerini ekle (ilk seferde bir kez)
python seed.py

# 2. Sunucuyu başlat
uvicorn main:app --reload --port 8000
```

Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Endpoint'leri

### Makineler

| Method | URL | Açıklama |
|--------|-----|----------|
| GET | `/api/machines` | Tüm makineleri listele |
| GET | `/api/machines/{id}` | Tek makine getir |
| PUT | `/api/machines/{id}/status` | Makine durumunu güncelle |

**PUT body:**
```json
{ "status": "RUNNING" }
```

Geçerli status değerleri: `AVAILABLE`, `RUNNING`, `FINISHING`, `FINISHED`

---

### Sıra Sistemi

| Method | URL | Açıklama |
|--------|-----|----------|
| POST | `/api/queue` | Sıraya gir |
| GET | `/api/queue/machine/{id}` | Makinenin sırasını gör |
| DELETE | `/api/queue/{id}?student_id=xxx` | Sıradan çık |

**POST body:**
```json
{ "machine_id": 1, "student_id": "2021123456" }
```

---

## MQTT

Broker: `test.mosquitto.org:1883`  
Topic: `laundry/machine/#`

ESP32'den beklenen JSON formatı:
```json
{
  "device_id": "esp32_001",
  "vibration": 2.45
}
```

`device_id` değerleri `seed.py`'deki `esp32_001`, `esp32_002`, `esp32_003` ile eşleşmeli.

Titreşim eşikleri (`services/analysis.py`):

| Ortalama | Durum |
|----------|-------|
| > 1.5 g | RUNNING |
| < 0.5 g | AVAILABLE |
| Arada | FINISHING |

---

## Veritabanı Şeması

**machines**

| Kolon | Tip | Açıklama |
|-------|-----|----------|
| id | INTEGER PK | Otomatik artar |
| name | VARCHAR(50) | Makine adı |
| status | VARCHAR(20) | AVAILABLE / RUNNING / FINISHING / FINISHED |
| esp_device_id | VARCHAR(50) | ESP32 cihaz kimliği (unique) |
| last_update | DATETIME | Son güncelleme zamanı |

**queue**

| Kolon | Tip | Açıklama |
|-------|-----|----------|
| id | INTEGER PK | Otomatik artar |
| machine_id | INTEGER FK | machines.id |
| student_id | VARCHAR(20) | Öğrenci numarası |
| created_at | DATETIME | Sıraya girme zamanı |
| status | VARCHAR(20) | WAITING / NOTIFIED / COMPLETED / CANCELLED |

---

## Testler

```bash
pytest tests/ -v
```

25 test, tümü geçiyor. Kapsam: machine endpoint'leri, sıra sistemi, titreşim analizi.

---

## Dosya Yapısı

```
backend/
├── main.py               # FastAPI app, lifespan, CORS
├── database.py           # SQLAlchemy bağlantısı
├── models.py             # Machine ve Queue modelleri
├── seed.py               # Başlangıç verisi
├── routes/
│   ├── machines.py       # Makine endpoint'leri
│   └── queue.py          # Sıra endpoint'leri
└── services/
    ├── analysis.py       # Titreşim analizi (pandas)
    └── mqtt_handler.py   # MQTT listener (paho-mqtt)
```
