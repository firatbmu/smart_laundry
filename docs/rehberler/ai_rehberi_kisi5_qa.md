# AI Kullanim Rehberi - Kisi 5 (QA Engineer & Documentation)

Bu rehber, yapay zeka asistani kullanarak gorevlerini tamamlamani saglayacak.

---

## Temel Kullanim Kurallari

1. **Gorevi AI'a yapistir**
2. **"Adim adim anlat" de**
3. **Kodu al, calistir**
4. **Hata varsa hatayi yapistir**
5. **Calisana kadar tekrarla**

---

# HAFTA 1: Git ve GitHub

## Gorev 1.1: Git Nedir?

### Prompt:
```
Git nedir? Ne ise yarar?
Versiyon kontrolu ne demek?
Neden Git kullaniriz?
GitHub ile Git farki ne?
Basit ve anlasilir anlat, yeni baslayanlara uygun.
```

---

## Gorev 1.2: Git Kurulumu

### Prompt:
```
Windows'a Git nasil kurulur?
Adim adim anlat.
Kurulumu dogrulamak icin terminal komutu ver.
git --version ne dondurmeli?
```

---

## Gorev 1.3: Git Clone

### Prompt:
```
git clone komutu ne yapar?
GitHub'dan repo nasil indirilir?
Ornek komut:
git clone https://github.com/kullanici/smart-laundry.git
Clone ettikten sonra ne yapmaliyim?
```

---

## Gorev 1.4: Git Add, Commit, Push

### Prompt:
```
Git'te degisiklikleri nasil kaydederim?
3 adimi acikla:
1. git add - degisiklikleri hazirla
2. git commit - degisiklikleri kaydet
3. git push - GitHub'a gonder
Her adim icin ornek komut ver.
Commit mesaji nasil yazilmali?
```

### Ornek Komutlar:
```bash
git add .
git commit -m "README dosyasi eklendi"
git push origin main
```

---

## Gorev 1.5: Git Pull

### Prompt:
```
git pull komutu ne yapar?
Ne zaman kullanilir?
Takim arkadasim degisiklik yapti, nasil alirim?
Ornek komut ver.
```

---

## Gorev 1.6: Branch Olusturma

### Prompt:
```
Git'te branch (dal) nedir?
Neden kullanilir?
Yeni branch nasil olusturulur?
Branch'ler arasi nasil gecilir?
Ornek senaro:
- main branch: kararli kod
- feature/readme branch: yeni ozellik
Komutlari ver.
```

### Ornek Komutlar:
```bash
git checkout -b feature/readme
# ... degisiklikler yap ...
git add .
git commit -m "README guncellendi"
git push origin feature/readme
```

---

## Gorev 1.7: Pull Request (PR)

### Prompt:
```
Pull Request (PR) nedir?
Ne ise yarar?
GitHub'da PR nasil acilir?
PR aciklama metni nasil yazilmali?
Adim adim anlat.
```

---

## Gorev 1.8: Merge Conflict

### Prompt:
```
Git'te merge conflict nedir?
Ne zaman olur?
Conflict nasil cozulur?
Adim adim anlat.
Ornek conflict senaryosu ve cozumu goster.
```

---

## Gorev 1.9: README.md Temelleri

### Prompt:
```
README.md dosyasi nedir?
Ne icin kullanilir?
Iyi bir README'de neler olmali?
Basit bir README sablonu ver.
```

---

# HAFTA 2: Python Temelleri

## Gorev 2.1: Python Kurulumu

### Prompt:
```
Windows'a Python 3.12 nasil kurulur?
PATH'e otomatik eklensin.
Terminal'de "python --version" komutu ne dondurmeli?
Adim adim anlat.
```

---

## Gorev 2.2: Python Degiskenleri

### Prompt:
```
Python'da degisken nedir?
Nasil tanimlanir?
Veri tipleri: string, int, float, bool
Her biri icin ornek kod yaz.
```

---

## Gorev 2.3: Fonksiyonlar

### Prompt:
```
Python'da fonksiyon nasil yazilir?
def anahtar kelimesi
Parametre alma
return ile deger dondurme
3 basit fonksiyon ornegi yaz:
1. Iki sayi topla
2. Isim alip selam ver
3. Sayinin tek/cift oldugunu soyle
```

---

## Gorev 2.4: Dosya Okuma/Yazma

### Prompt:
```
Python'da dosya nasil okunur?
Python'da dosya nasil yazilir?
open() fonksiyonu
with blogu neden kullanilir?
Ornek: metin dosyasi oku ve ekrana yazdir.
Ornek: listeyi dosyaya yaz.
```

---

## Gorev 2.5: requirements.txt

### Prompt:
```
Python'da requirements.txt nedir?
Ne ise yarar?
Nasil olusturulur? (pip freeze > requirements.txt)
Nasil kullanilir? (pip install -r requirements.txt)
Proje icin ornek requirements.txt yaz.
```

---

# HAFTA 3: Markdown ve Dokumantasyon

## Gorev 3.1: Markdown Nedir?

### Prompt:
```
Markdown nedir?
Nerede kullanilir? (GitHub, dokumantasyon)
Neden duz metin yerine Markdown?
Temel avantajlari neler?
```

---

## Gorev 3.2: Markdown Sozdizimi

### Prompt:
```
Markdown temel sozdizimini ogret.
Basliklar: # ## ###
Kalin: **metin**
Italik: *metin*
Liste: - madde
Numarali liste: 1. madde
Kod blogu: ```python kod ```
Link: [metin](url)
Resim: ![alt](url)
Her biri icin ornek ver.
```

---

## Gorev 3.3: README.md Sablonu

### Prompt:
```
Akilli Camasirhane projesi icin README.md sablonu olustur.
Bolumler:
1. Proje Adi ve Aciklama
2. Ozellikler
3. Kurulum
4. Kullanim
5. API Dokumantasyonu
6. Takim
7. Lisans
Her bolum icin ornekler ekle.
```

---

## Gorev 3.4: Proje Aciklamasi Yazma

### Prompt:
```
Akilli Camasirhane projesi icin aciklama yaz.
Icerik:
- Proje ne yapiyor?
- Hangi problemi cozuyor?
- Nasil calisir? (kisa)
- Hangi teknolojiler kullaniliyor?
2-3 paragraf, acik ve anlasilir.
```

---

## Gorev 3.5: Kurulum Adimlari

### Prompt:
```
Proje kurulum adimlarini yaz.
Backend icin:
1. Python kurulumu
2. Repo clone
3. Virtual environment
4. Paket yukleme
5. Veritabani olusturma
6. Server baslatma
Her adim icin komut ornekleri ekle.
```

---

## Gorev 3.6: GitHub Wiki

### Prompt:
```
GitHub Wiki nedir?
Ne ise yarar?
Wiki sayfasi nasil olusturulur?
Proje icin Wiki yapisi onerisi ver.
```

---

# HAFTA 4: Pytest Temelleri

## Gorev 4.1: Test Nedir?

### Prompt:
```
Yazilim testi nedir?
Neden test yazariz?
Unit test ne demek?
Test yazmak zaman kaybi mi?
Basit ve ikna edici anlat.
```

---

## Gorev 4.2: Pytest Kurulumu

### Prompt:
```
Python'da pytest nasil kurulur?
pip install pytest
Kurulumu dogrulama:
pytest --version
Basit bir test dosyasi olustur ve calistir.
```

---

## Gorev 4.3: Ilk Test

### Prompt:
```
Pytest ile ilk test fonksiyonunu yaz.
Dosya: test_example.py
Test: toplama fonksiyonunu test et.
assert ne demek?
Testin gectigini/kaldigini nasil anlarim?
```

### Ornek Kod:
```python
# test_example.py

def topla(a, b):
    return a + b

def test_topla():
    assert topla(2, 3) == 5
    assert topla(-1, 1) == 0
    assert topla(0, 0) == 0
```

---

## Gorev 4.4: Assert Kullanimi

### Prompt:
```
Pytest'te assert nasil kullanilir?
Farkli assert ornekleri:
- Esitlik kontrolu
- Buyukluk/kuculuk
- Liste icinde eleman kontrolu
- Exception firlatma kontrolu
Her biri icin ornek kod yaz.
```

---

## Gorev 4.5: Test Dosya Organizasyonu

### Prompt:
```
Test dosyalari nasil organize edilmeli?
tests/ klasoru yapisi
test_*.py isimlendirme kurali
__init__.py gerekli mi?
Ornek klasor yapisi goster.
```

### Ornek Yapi:
```
tests/
├── __init__.py
├── test_api.py
├── test_models.py
├── test_mqtt.py
└── test_utils.py
```

---

## Gorev 4.6: pytest Calistirma

### Prompt:
```
pytest nasil calistirilir?
Tum testleri calistir: pytest
Tek dosya: pytest test_api.py
Tek fonksiyon: pytest test_api.py::test_get_machines
Verbose mod: pytest -v
Ciktilari goster: pytest -s
Orneklerle anlat.
```

---

# HAFTA 5: API Testleri

## Gorev 5.1: Flask Test Client

### Prompt:
```
Flask uygulamasini nasil test ederim?
Flask test client nedir?
app.test_client() nasil kullanilir?
Basit ornek: GET / endpoint testi.
```

---

## Gorev 5.2: test_api.py Olusturma

### Prompt:
```
Flask API testleri icin dosya olustur.
Dosya: tests/test_api.py
Icerik:
- Test client fixture
- test_get_machines()
- test_get_machine_by_id()
- test_update_status()
Her test icin assert'lar ekle.
```

### Ornek Kod:
```python
import pytest
from app import app, db
from models import Machine

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_machines(client):
    response = client.get('/api/machines')
    assert response.status_code == 200
    data = response.get_json()
    assert 'machines' in data
```

---

## Gorev 5.3: test_get_machines

### Prompt:
```
GET /api/machines endpoint testi yaz.
Test senaryolari:
1. Bos veritabani -> bos liste doner
2. 3 makine ekle -> 3 elemanli liste doner
3. Her makinenin id, name, status alanlari var
Her senaryo icin test fonksiyonu yaz.
```

---

## Gorev 5.4: test_update_status

### Prompt:
```
PUT /api/machines/{id}/status endpoint testi yaz.
Test senaryolari:
1. Basarili guncelleme -> 200
2. Makine bulunamadi -> 404
3. Gecersiz status -> 400
Her senaryo icin test fonksiyonu yaz.
```

---

## Gorev 5.5: Hata Senaryolari

### Prompt:
```
API hata senaryolarini test et.
Test edilecek durumlar:
1. 404 Not Found (olmayan makine ID'si)
2. 400 Bad Request (eksik/yanlis veri)
3. Gecersiz status degeri
Her biri icin test fonksiyonu yaz.
```

---

# HAFTA 6: Entegrasyon Testleri

## Gorev 6.1: End-to-End Test Nedir?

### Prompt:
```
End-to-end (E2E) test nedir?
Unit test'ten farki ne?
Bizim projede E2E test nasil olur?
Sensor -> Backend -> Mobil akisi nasil test edilir?
```

---

## Gorev 6.2: Sensor Hesaplama Testi

### Prompt:
```
Titresim hesaplama fonksiyonunu test et.
Fonksiyon: sqrt(ax^2 + ay^2 + az^2) - 1.0
Test senaryolari:
1. ax=0, ay=0, az=1 -> vibration = 0 (hareketsiz)
2. ax=1, ay=1, az=1 -> vibration > 0 (hareket var)
3. Negatif degerler de calisir
pytest ile test yaz.
```

---

## Gorev 6.3: Veritabani Testleri

### Prompt:
```
SQLAlchemy modelleri icin test yaz.
Test edilecekler:
1. Machine olusturma
2. Machine status guncelleme
3. Birden fazla makine ekleme
4. Machine sorgulama (ID ile, status ile)
In-memory SQLite kullan.
```

---

## Gorev 6.4: Test Coverage

### Prompt:
```
Test coverage nedir?
Neden onemli?
pytest-cov nasil kurulur ve kullanilir?
Coverage raporu nasil olusturulur?
%80 coverage iyi mi?
```

### Ornek Komut:
```bash
pip install pytest-cov
pytest --cov=app --cov-report=html
```

---

## Gorev 6.5: Bug Tracking

### Prompt:
```
GitHub Issues ile bug tracking nasil yapilir?
Issue nasil acilir?
Issue template nasil olusturulur?
Bug raporu nasil yazilmali?
Ornek bug raporu ver.
```

### Ornek Bug Raporu:
```markdown
## Bug: Makine durumu guncellenmiyor

**Adimlar:**
1. GET /api/machines cagir
2. PUT /api/machines/1/status ile durum guncelle
3. Tekrar GET /api/machines cagir

**Beklenen:** Durum "RUNNING" olmali
**Gerceklesen:** Durum hala "AVAILABLE"

**Ortam:** Python 3.12, Flask 3.0, Windows

**Log:**
[hata mesaji varsa]
```

---

## Gorev 6.6: Test Raporu

### Prompt:
```
Test sonuclarini raporla.
Markdown formatinda test raporu yaz.
Icerik:
- Toplam test sayisi
- Gecen/kalan testler
- Coverage yuzdesi
- Bilinen hatalar
- Oneriler
```

---

# HAFTA 7: Dokumantasyon + Sira Sistemi Testleri

> **BONUS OZELLIK:** Bu hafta, temel sistem dokumantasyonunu tamamlayacak ve Hafta 7'de eklenen sira sistemi icin testler yazacaksin.

---

## Gorev 7.1: Sira API Testleri

### Prompt:
```
Sira sistemi API testleri yaz.
Test edilecek endpoint'ler:
- POST /api/queue (siraya gir)
- GET /api/queue/machine/{id} (sira listesi)
- DELETE /api/queue/{id} (siradan cik)
Her biri icin basarili ve basarisiz senaryolar.
pytest ile yaz.
```

### Beklenen Test Ornegi:
```python
def test_join_queue(client):
    """Siraya girme testi"""
    response = client.post('/api/queue', json={
        'machine_id': 1,
        'student_id': '2021123456'
    })
    assert response.status_code == 201
    assert 'position' in response.json

def test_duplicate_queue_entry(client):
    """Ayni kisi iki kez siraya giremez"""
    client.post('/api/queue', json={
        'machine_id': 1,
        'student_id': '2021123456'
    })
    response = client.post('/api/queue', json={
        'machine_id': 1,
        'student_id': '2021123456'
    })
    assert response.status_code == 400
```

---

## Gorev 7.2: Queue Veritabani Testleri

### Prompt:
```
Queue modeli icin veritabani testleri yaz.
Test edilecekler:
1. Queue olusturma (foreign key ile)
2. Queue status guncelleme
3. Machine-Queue iliskisi
4. Sira sorgulama (created_at sirasina gore)
In-memory SQLite kullan.
```

---

## Gorev 7.3: README.md Tamamlama

### Prompt:
```
README.md dosyasini tamamla.
Kontrol listesi:
[ ] Proje aciklamasi
[ ] Ozellikler listesi
[ ] Kurulum adimlari (Backend, Mobile, Hardware)
[ ] Kullanim ornekleri
[ ] API endpoint listesi
[ ] Ekran goruntuleri (opsiyonel)
[ ] Takim bilgileri
[ ] Lisans
Eksikleri tamamla.
```

---

## Gorev 7.4: API Dokumantasyonu

### Prompt:
```
API dokumantasyonu yaz.
Kisi 2 ile birlikte.
Her endpoint icin:
- HTTP metodu ve URL
- Aciklama
- Request body (varsa)
- Response ornegi
- Hata kodlari
Markdown formatinda.
```

### Ornek:
```markdown
## GET /api/machines

Tum makinelerin listesini dondurur.

**Response:**
```json
{
  "machines": [
    {
      "id": 1,
      "name": "Makine 1",
      "status": "AVAILABLE",
      "last_update": "2024-01-15T14:30:00"
    }
  ]
}
```

**Status Codes:**
- 200: Basarili
- 500: Server hatasi
```

---

## Gorev 7.5: Donanim Dokumantasyonu

### Prompt:
```
Donanim baglanti dokumantasyonu yaz.
Kisi 1 ile birlikte.
Icerik:
- Gerekli malzemeler listesi
- ESP32 - MPU6050 baglanti semasi
- Pin baglantilari tablosu
- Kurulum adimlari
- Sorun giderme
Markdown formatinda, resim olmadan.
```

---

## Gorev 7.6: Kurulum Rehberi

### Prompt:
```
Detayli kurulum rehberi yaz.
Bolumler:
1. Gereksinimler (Python, Git, vs.)
2. Backend Kurulumu
3. Mobile Kurulumu
4. Hardware Kurulumu
5. Tum sistemi calistirma
Her adim icin komut ornekleri ekle.
```

---

## Gorev 7.7: Troubleshooting

### Prompt:
```
Sik karsilasan sorunlar ve cozumleri yaz.
Kategoriler:
1. Kurulum sorunlari
2. Backend sorunlari
3. Mobile sorunlari
4. Hardware sorunlari
5. Baglanti sorunlari
Her sorun icin: Belirti, Neden, Cozum.
```

---

# HAFTA 8: Sunum Hazirligi

## Gorev 8.1: Sunum Slaytlari

### Prompt:
```
Proje sunumu icin slayt icerigi olustur.
10-15 slayt.
Icerik:
1. Baslik slayt (proje adi, takim)
2. Problem tanimi
3. Cozum/Proje aciklamasi
4. Sistem mimarisi
5. Teknik detaylar
6. Demo (ekran goruntuleri/video)
7. Zorluklar ve ogrendiklerimiz
8. Gelecek planlar
9. Soru-cevap
Her slayt icin bullet point'ler yaz.
```

---

## Gorev 8.2: Demo Senaryosu

### Prompt:
```
3 dakikalik demo senaryosu yaz.
Adimlar:
1. Mobil uygulamayi ac (30 sn)
2. Makine listesini goster (30 sn)
3. Bir makineyi calistir (breadboard simule) (30 sn)
4. Durum degisimini goster (30 sn)
5. Siraya gir, sirani goster (30 sn)
6. Kapani (30 sn)
Her adim icin ne soylenecek yaz.
```

---

## Gorev 8.3: Sunum Provasi

### Prompt:
```
Sunum provasi nasil organize edilmeli?
Kontrol listesi:
[ ] Herkes kendi bolumunu biliyor
[ ] Teknik ekipman calisiyor (laptop, projektor)
[ ] Demo hazir
[ ] Yedek plan var
[ ] Zamanlama uygun
[ ] Soru-cevap hazirligi
Prova plani olustur.
```

---

## Gorev 8.4: Yedek Plan

### Prompt:
```
Demo sirasinda sorun cikarsa yedek plan ne?
Senaryolar:
1. WiFi calismadi
2. Backend crashledi
3. ESP32 baglanti koptu
4. Mobil uygulama acilmadi
Her senaryo icin yedek plan yaz.
```

---

## Gorev 8.5: Soru-Cevap Hazirligi

### Prompt:
```
Sunumda sorulabilecek sorular ve cevaplari hazirla.
Muhtemel sorular:
1. Neden bu teknolojiyi sectiniz?
2. Gercek ortamda nasil calisir?
3. Guvenlik nasil saglandi?
4. Olceklenebilir mi?
5. Gelecekte ne eklenebilir?
Her soru icin kisa ve net cevap yaz.
```

---

# SIK KARSILASILAN HATALAR

## Hata 1: Git Push Rejected
```
Prompt: "git push yaparken 'rejected' hatasi aliyorum.
'Updates were rejected because the remote contains work...'
Ne yapmaliyim? git pull mi cekmeliyim?
Force push tehlikeli mi?"
```

## Hata 2: Merge Conflict
```
Prompt: "Git merge conflict olustu.
Dosyada <<<<<<< HEAD isaretleri var.
Nasil cozerim?
Adim adim anlat."
```

## Hata 3: pytest Module Not Found
```
Prompt: "pytest calistirinca 'ModuleNotFoundError' aliyo rum.
'No module named app' diyor.
PYTHONPATH ayari mi lazim?
Nasil cozerim?"
```

## Hata 4: Test Fixture Hatasi
```
Prompt: "pytest fixture calismadi.
'fixture not found' hatasi.
@pytest.fixture decorator'u ekledim.
Neden bulamiyor?"
```

## Hata 5: Coverage 0%
```
Prompt: "pytest-cov calistirdim ama coverage 0% gorunuyor.
Testler geciyor ama coverage olculmuyor.
--cov parametresi yanlis mi?"
```

---

# DOKUMANTASYON IPUCLARI

```
Prompt: "Iyi dokumantasyon nasil yazilir?
Best practices neler?
Cok uzun mu kisa mi olmali?
Kod ornekleri ne kadar olmali?
Hedef kitle kim?"
```

---

# YARDIM ISTEME SABLONU

Takildiginda su formati kullan:

```
SORUN: [Ne yapmaya calisiyorsun]
HATA: [Tam hata mesaji]
DENEDIKLERIM: [Simdiye kadar ne denedin]
ORTAM: Python 3.12, pytest, Windows
KOMUT: [Calistirdigin komut]
KOD: [Ilgili kod parcasi]
```

---

**Basarilar!**
