# AI Kullanim Rehberi - Kisi 2 (Backend Developer)

Bu rehber, yapay zeka asistani kullanarak gorevlerini tamamlamani saglayacak.

---

## Temel Kullanim Kurallari

1. **Gorevi AI'a yapistir**
2. **"Adim adim anlat" de**
3. **Kodu al, calistir**
4. **Hata varsa hatayi yapistir**
5. **Calisana kadar tekrarla**

---

# HAFTA 1: Ortam Kurulumu

## Gorev 1.1: Python Kurulumu

### Prompt:
```
Windows'a Python 3.12 nasil kurulur?
Adim adim anlat.
PATH'e ekleme secenegini unutma.
Kurulumu dogrulamak icin terminal komutunu ver.
```

### Dogrulama:
```bash
python --version
# Cikti: Python 3.12.x olmali
```

---

## Gorev 1.2: VS Code Kurulumu

### Prompt:
```
VS Code'u Windows'a kur.
Python extension'i yukle.
Python interpreter'i nasil secerim?
Terminal'de Python nasil calistiririm?
Adim adim anlat.
```

---

## Gorev 1.3: Git Temelleri

### Prompt:
```
Git nedir? Neden kullanilir?
Temel komutlari acikla:
- git clone
- git add
- git commit
- git push
- git pull
Basit orneklerle anlat, yeni baslayanlar icin.
```

---

## Gorev 1.4: Virtual Environment

### Prompt:
```
Python virtual environment nedir?
Neden kullanilir?
Windows'ta nasil olusturulur?
Aktif/pasif nasil yapilir?
requirements.txt nasil kullanilir?
Komutlari ver.
```

### Beklenen Komutlar:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Gorev 1.5: Repo Clone ve Kurulum

### Prompt:
```
GitHub'dan repo nasil clone edilir?
Repo URL'si: https://github.com/takim/smart-laundry
Clone ettikten sonra:
1. Virtual environment olustur
2. Paketleri yukle
Windows komutlarini ver.
```

---

# HAFTA 2: Flask Temelleri

## Gorev 2.1: Flask Nedir?

### Prompt:
```
Flask nedir?
Web framework ne demek?
Django'dan farki ne?
Neden Flask sectik?
Basit ve kisa anlat.
```

---

## Gorev 2.2: Hello World

### Prompt:
```
Flask ile "Hello World" uygulamasi yaz.
Dosya adi: app.py
http://localhost:5000 adresinde calissin.
Kodu yaz ve nasil calistirilacagini anlat.
```

### Beklenen Kod:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Gorev 2.3: Route ve Endpoint

### Prompt:
```
Flask'ta route ne demek?
Endpoint ne demek?
Farkli route'lar nasil tanimlanir?
Ornekler ver:
- / -> Ana sayfa
- /about -> Hakkinda
- /api/test -> API test
```

---

## Gorev 2.4: JSON Response

### Prompt:
```
Flask'ta JSON response nasil dondurulur?
jsonify fonksiyonunu acikla.
Ornek endpoint yaz:
GET /api/status -> {"status": "ok", "message": "Server calisiyor"}
```

---

## Gorev 2.5: Postman Kullanimi

### Prompt:
```
Postman nedir? Ne ise yarar?
Windows'a nasil kurulur?
Flask API'yi Postman ile nasil test ederim?
GET ve POST istegi nasil yapilir?
Adim adim anlat.
```

---

# HAFTA 3: Veritabani ve SQLAlchemy

## Gorev 3.1: SQLAlchemy Nedir?

### Prompt:
```
SQLAlchemy nedir?
ORM ne demek?
Neden direkt SQL yazmak yerine ORM kullaniriz?
Flask-SQLAlchemy nedir?
Basit anlat.
```

---

## Gorev 3.2: Veritabani Baglantisi

### Prompt:
```
Flask'ta SQLite veritabani nasil baglanir?
Flask-SQLAlchemy kullan.
app.py'de konfigurasyonu yaz.
Veritabani dosyasi: laundry.db
```

### Beklenen Kod:
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laundry.db'
db = SQLAlchemy(app)
```

---

## Gorev 3.3: Machine Modeli

### Prompt:
```
Flask-SQLAlchemy ile Machine modeli olustur.
Dosya: models.py
Alanlar:
- id (integer, primary key, auto increment)
- name (string, max 50 karakter, ornek: "Makine 1")
- status (string, max 20, ornek: "AVAILABLE", "RUNNING", "FINISHED")
- esp_device_id (string, max 50, ornek: "esp32_001")
- last_update (datetime, otomatik guncellenen)

Modeli yaz ve acikla.
```

---

## Gorev 3.4: Veritabani Olusturma

### Prompt:
```
Flask-SQLAlchemy ile tablo nasil olusturulur?
db.create_all() nasil kullanilir?
Terminalde Python shell ile nasil yaparim?
Adim adim anlat.
```

### Beklenen Komutlar:
```python
from app import app, db
from models import Machine

with app.app_context():
    db.create_all()
    print("Tablolar olusturuldu!")
```

---

## Gorev 3.5: CRUD Islemleri

### Prompt:
```
SQLAlchemy ile temel CRUD islemlerini goster.
Model: Machine
Ornekler:
1. Create: Yeni makine ekle
2. Read: Tum makineleri listele
3. Read: ID ile tek makine getir
4. Update: Makine durumunu guncelle
5. Delete: Makine sil
Her biri icin kod ornegi ver.
```

---

# HAFTA 4: REST API Endpoint'leri

## Gorev 4.1: REST API Nedir?

### Prompt:
```
REST API nedir?
HTTP metodlari ne anlama gelir:
- GET
- POST
- PUT
- DELETE
Her biri icin gercek hayat ornegi ver.
```

---

## Gorev 4.2: GET /api/machines

### Prompt:
```
Flask ile GET /api/machines endpoint'i yaz.
SQLite veritabanindan Machine tablosunu cek.
JSON olarak dondur.
Ornek response:
{
  "machines": [
    {"id": 1, "name": "Makine 1", "status": "AVAILABLE"},
    {"id": 2, "name": "Makine 2", "status": "RUNNING"}
  ]
}
```

### Beklenen Kod:
```python
@app.route('/api/machines', methods=['GET'])
def get_machines():
    machines = Machine.query.all()
    result = []
    for m in machines:
        result.append({
            'id': m.id,
            'name': m.name,
            'status': m.status,
            'last_update': m.last_update.isoformat() if m.last_update else None
        })
    return jsonify({'machines': result})
```

---

## Gorev 4.3: GET /api/machines/{id}

### Prompt:
```
Flask ile GET /api/machines/<id> endpoint'i yaz.
URL'den id parametresini al.
Veritabanindan o ID'li makineyi getir.
Bulunamazsa 404 hatasi dondur.
JSON response ornegi ver.
```

---

## Gorev 4.4: PUT /api/machines/{id}/status

### Prompt:
```
Flask ile PUT /api/machines/<id>/status endpoint'i yaz.
Request body:
{"status": "RUNNING"}
Makine durumunu guncelle.
last_update'i simdi olarak ayarla.
Basarili: 200 + guncellenmis makine
Hata: 404 (makine yok) veya 400 (gecersiz status)
```

---

## Gorev 4.5: Hata Handling

### Prompt:
```
Flask'ta hata yonetimi nasil yapilir?
404 Not Found nasil dondurulur?
400 Bad Request nasil dondurulur?
500 Internal Server Error nasil yakalanir?
Ornek kodlar ver.
```

---

## Gorev 4.6: routes/machines.py Ayirma

### Prompt:
```
Flask'ta route'lari ayri dosyaya nasil tasarim?
Blueprint nedir?
app.py'deki machine endpoint'lerini
routes/machines.py dosyasina tasi.
Dosya yapisini ve kodu goster.
```

---

# HAFTA 5: MQTT Entegrasyonu

## Gorev 5.1: MQTT Nedir? (Backend Perspektifi)

### Prompt:
```
MQTT nedir? Backend tarafinda nasil kullanilir?
paho-mqtt kutuphanesi ne ise yarar?
Subscribe (dinleme) nasil yapilir?
ESP32'den gelen veriyi Python'da nasil alirim?
```

---

## Gorev 5.2: paho-mqtt Kurulumu

### Prompt:
```
Python'da paho-mqtt kutuphanesini nasil kurarim?
pip komutu ver.
requirements.txt'e nasil eklerim?
```

---

## Gorev 5.3: MQTT Subscriber

### Prompt:
```
Python ile MQTT subscriber yaz.
paho-mqtt kullan.
Broker: test.mosquitto.org
Port: 1883
Topic: laundry/machine/#
Gelen mesajlari ekrana yazdir.
Baglanti durumunu goster.
```

---

## Gorev 5.4: JSON Parse

### Prompt:
```
MQTT'den gelen JSON mesajini parse et.
Ornek mesaj:
{
  "device_id": "esp32_001",
  "vibration": 2.45,
  "status": "RUNNING"
}
Python ile bu veriyi oku ve isleme al.
Hata durumunda (gecersiz JSON) nasil handle edilir?
```

---

## Gorev 5.5: Veritabani Guncelleme

### Prompt:
```
MQTT'den gelen veriyle veritabanini guncelle.
Adimlar:
1. device_id'ye gore makineyi bul
2. status'u guncelle
3. last_update'i simdi yap
4. db.session.commit()
Flask-SQLAlchemy ile kodu yaz.
```

---

## Gorev 5.6: mqtt_handler.py Servisi

### Prompt:
```
Flask uygulamasiyla birlikte calisan MQTT handler yaz.
Dosya: services/mqtt_handler.py
Threading kullanarak ayri thread'de calissin.
Flask app context'i icerisinde veritabani erissin.
start_mqtt_listener() fonksiyonu yaz.
```

---

# HAFTA 6: Pandas ve Veri Analizi

## Gorev 6.1: Pandas Nedir?

### Prompt:
```
Pandas kutuphanesi nedir?
DataFrame ne demek?
Neden kullaniyoruz?
Basit orneklerle anlat.
```

---

## Gorev 6.2: Pandas Kurulumu

### Prompt:
```
Python'a pandas nasil yuklenir?
pip komutu ver.
Basit bir DataFrame ornegi goster.
```

---

## Gorev 6.3: Titresim Analizi

### Prompt:
```
Pandas ile titresim verisi analizi yap.
Veriler: [2.3, 2.5, 2.1, 0.3, 0.2, 0.4, 2.8, 2.6]
Hesapla:
- Ortalama
- Standart sapma
- Min/Max
- Son 5 verinin ortalamasi
Kodu yaz.
```

---

## Gorev 6.4: Durum Tespiti Servisi

### Prompt:
```
Titresim verisinden makine durumu tespit eden fonksiyon yaz.
Input: Son 10 titresim verisi (liste)
Output: "AVAILABLE", "RUNNING", veya "FINISHING"
Pandas kullan.
Kurallar:
- Ortalama > 1.5 -> RUNNING
- Ortalama < 0.5 -> AVAILABLE
- Arada -> FINISHING
```

---

## Gorev 6.5: CORS Ayarlari

### Prompt:
```
Flask'ta CORS nedir?
Neden gerekli?
flask-cors nasil kurulur ve kullanilir?
Tum origin'lere izin ver.
Kodu goster.
```

---

## Gorev 6.6: API Dokumantasyonu

### Prompt:
```
REST API dokumantasyonu nasil yazilir?
Markdown formatinda yaz.
Icerik:
- Base URL
- Authentication (simdilik yok)
- Endpoints listesi
- Her endpoint icin: method, URL, request body, response ornegi
Ornek: GET /api/machines
```

---

# HAFTA 7: Sira Sistemi API

> **BONUS OZELLIK:** Bu hafta, temel sistem tamamlandiktan sonra eklenen sira sistemi ozelligini gelistireceksin. Hafta 1-6'da makine durumu takibi tamamlandi, simdi kullanicilar dolu makineler icin siraya girebilecek.

---

## Gorev 7.1: Queue Modeli

### Prompt:
```
Flask-SQLAlchemy ile Queue (sira) modeli olustur.
Alanlar:
- id (integer, primary key)
- machine_id (integer, foreign key -> Machine.id)
- student_id (string, max 20, ogrenci no)
- created_at (datetime, olusturulma zamani)
- status (string: "WAITING", "NOTIFIED", "COMPLETED", "CANCELLED")

Machine ile iliskiyi (relationship) tanimla.
```

### Beklenen Kod:
```python
class Queue(db.Model):
    __tablename__ = 'queue'
    
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('machine.id'), nullable=False)
    student_id = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='WAITING')
    
    machine = db.relationship('Machine', backref='queue_entries')
```

### Veritabani Guncelleme:
```python
from app import app, db
from models import Machine, Queue

with app.app_context():
    db.create_all()
    print("Queue tablosu eklendi!")
```

---

## Gorev 7.2: POST /api/queue

### Prompt:
```
Flask ile POST /api/queue endpoint'i yaz.
Request body:
{
  "machine_id": 1,
  "student_id": "2021123456"
}
Yeni sira kaydi olustur.
Status: "WAITING"
Response: Olusturulan kayit + siradaki pozisyon
Ayni ogrenci ayni makineye iki kez eklenemesin.
```

---

## Gorev 7.3: GET /api/queue/machine/{id}

### Prompt:
```
Flask ile GET /api/queue/machine/<id> endpoint'i yaz.
O makinenin sira listesini dondur.
Sadece "WAITING" durumundakileri getir.
Siralama: created_at (en eski en basta)
Response ornegi ver.
```

---

## Gorev 7.4: DELETE /api/queue/{id}

### Prompt:
```
Flask ile DELETE /api/queue/<id> endpoint'i yaz.
Sira kaydini iptal et.
Status'u "CANCELLED" yap (silme yerine guncelle).
Sadece kendi kaydini iptal edebilsin (student_id kontrolu).
```

---

## Gorev 7.5: Sira Mantigi

### Prompt:
```
Makine bosaldiginda sira sistemini guncelle.
Adimlar:
1. Makine status "FINISHED" olunca
2. O makinenin ilk siradaki kisisini bul
3. Status'unu "NOTIFIED" yap
4. (Gelecekte: bildirim gonder)
Bu mantigi mqtt_handler'a entegre et.
```

---

## Gorev 7.6: Timeout Mekanizmasi

### Prompt:
```
Sira sistemi icin timeout ekle.
"NOTIFIED" olan kisi 5 dakika icinde gelmezse:
1. Status'u "EXPIRED" yap
2. Siradaki sonraki kisiye gec
Bu kontrolu periyodik olarak calistir.
Flask-APScheduler veya threading.Timer kullan.
```

---

# HAFTA 8: Test ve Dokumantasyon

## Gorev 8.1: API Test Stratejisi

### Prompt:
```
Flask API'yi nasil test ederim?
Flask test client nedir?
pytest ile nasil kullanilir?
Basit bir test ornegi ver.
```

---

## Gorev 8.2: Test Ornekleri

### Prompt:
```
Flask API icin pytest testleri yaz.
Test edilecek endpoint'ler:
1. GET /api/machines -> 200 + liste
2. GET /api/machines/999 -> 404
3. PUT /api/machines/1/status -> 200 + guncelleme
4. POST /api/queue -> 201 + yeni kayit
Her test icin kod yaz.
```

---

## Gorev 8.3: Dokumantasyon Tamamlama

### Prompt:
```
Backend API dokumantasyonunu tamamla.
Markdown formatinda.
Icerik:
1. Genel Bakis
2. Kurulum
3. Calistirma
4. API Endpoint'leri (tum detaylar)
5. Veritabani Semasi
6. MQTT Topic'leri
7. Hata Kodlari
```

---

# SIK KARSILASILAN HATALAR

## Hata 1: ModuleNotFoundError
```
Prompt: "Python'da 'ModuleNotFoundError: No module named flask' hatasi aliyorum.
pip install flask yaptim ama hala ayni hata.
Virtual environment aktif mi nasil anlarim?"
```

## Hata 2: Database Locked
```
Prompt: "SQLite 'database is locked' hatasi veriyor.
Birden fazla islem ayni anda veritabanina eriyor olabilir mi?
Nasil cozerim?"
```

## Hata 3: CORS Error
```
Prompt: "Frontend'den API'ye istek atinca 'CORS error' aliyorum.
Access-Control-Allow-Origin hatasi.
Flask'ta CORS nasil aktif edilir?"
```

## Hata 4: JSON Decode Error
```
Prompt: "MQTT'den gelen mesaji parse ederken 'JSONDecodeError' aliyorum.
Gelen veri: b'{"device_id": "esp32_001", ...}'
bytes'i string'e cevirip parse etmem mi lazim?"
```

## Hata 5: Circular Import
```
Prompt: "Flask'ta 'ImportError: cannot import name' hatasi aliyorum.
models.py ve app.py birbirini import ediyor.
Circular import nasil cozulur?"
```

---

# YARDIM ISTEME SABLONU

Takildiginda su formati kullan:

```
SORUN: [Ne yapmaya calisiyorsun]
HATA: [Tam hata mesaji]
DENEDIKLERIM: [Simdiye kadar ne denedin]
ORTAM: Python 3.12, Flask 3.x, Windows
KOD: [Ilgili kod parcasi]
```

---

**Basarilar!**
