# AI Kullanim Rehberi - Kisi 4 (Mobile Developer - Entegrasyon)

Bu rehber, yapay zeka asistani kullanarak gorevlerini tamamlamani saglayacak.

---

## Temel Kullanim Kurallari

1. **Gorevi AI'a yapistir**
2. **"Adim adim anlat" de**
3. **Kodu al, calistir**
4. **Hata varsa hatayi yapistir**
5. **Calisana kadar tekrarla**

---

# HAFTA 1: Python Temelleri

## Gorev 1.1: Python Kurulumu

### Prompt:
```
Windows'a Python 3.12 nasil kurulur?
PATH'e otomatik eklensin.
Kurulumu terminal'de nasil dogrularim?
Adim adim anlat.
```

---

## Gorev 1.2: Degiskenler

### Prompt:
```
Python'da degiskenler nasil tanimlanir?
String, integer, float, boolean nedir?
Her biri icin ornek kod yaz.
Degisken isimlendirme kurallari neler?
```

---

## Gorev 1.3: Listeler

### Prompt:
```
Python'da liste (list) nasil kullanilir?
Liste olusturma
Eleman ekleme, silme
for dongusuyle listeyi gezme
Ornek kodlar ver.
```

---

## Gorev 1.4: Sozlukler (Dictionary)

### Prompt:
```
Python'da dictionary (sozluk) nedir?
Key-value (anahtar-deger) yapisi nasil calisir?
Ornek:
makine = {
    "id": 1,
    "name": "Makine 1",
    "status": "AVAILABLE"
}
Sozlukten veri okuma ve yazma ornekleri ver.
```

---

## Gorev 1.5: Fonksiyonlar

### Prompt:
```
Python'da fonksiyon nasil yazilir?
def anahtar kelimesi
Parametre alma ve deger dondurme
Ornek: iki sayiyi toplayan fonksiyon
Ornek: listedeki en buyuk sayiyi bulan fonksiyon
```

---

## Gorev 1.6: Git Temelleri

### Prompt:
```
Git nedir? Neden kullanilir?
Temel komutlar:
- git clone
- git add
- git commit
- git push
- git pull
Basit aciklamalarla anlat.
```

---

# HAFTA 2: HTTP ve JSON

## Gorev 2.1: HTTP Nedir?

### Prompt:
```
HTTP protokolu nedir?
Web nasil calisir?
Client ve Server ne demek?
Request ve Response nedir?
Basit ve anlasilir anlat.
```

---

## Gorev 2.2: HTTP Metodlari

### Prompt:
```
HTTP metodlari nelerdir?
GET - veri almak
POST - veri gondermek
PUT - veri guncellemek
DELETE - veri silmek
Her biri icin gercek hayat ornegi ver.
```

---

## Gorev 2.3: JSON Formati

### Prompt:
```
JSON nedir?
Nasil yazilir?
Ornek JSON:
{
    "makineler": [
        {"id": 1, "name": "Makine 1", "status": "AVAILABLE"},
        {"id": 2, "name": "Makine 2", "status": "RUNNING"}
    ]
}
Python'da JSON nasil okunur ve yazilir?
json modulu kullanimi.
```

---

## Gorev 2.4: requests Kutuphanesi

### Prompt:
```
Python requests kutuphanesi nedir?
Nasil kurulur? (pip install requests)
GET istegi nasil yapilir?
POST istegi nasil yapilir?
Response nasil okunur?
Ornek kodlar ver.
```

### Ornek Kod:
```python
import requests

# GET istegi
response = requests.get('https://api.example.com/machines')
data = response.json()
print(data)

# POST istegi
new_data = {"machine_id": 1, "student_id": "123"}
response = requests.post('https://api.example.com/queue', json=new_data)
print(response.status_code)
```

---

## Gorev 2.5: API'den Veri Cekme

### Prompt:
```
Ucretsiz bir API'den veri cek.
API: https://jsonplaceholder.typicode.com/todos
GET istegi yap.
Response'u ekrana yazdir.
JSON'u Python dictionary'ye cevir.
```

---

## Gorev 2.6: Hata Kontrolu

### Prompt:
```
HTTP isteklerinde hata kontrolu nasil yapilir?
Status code'lar ne anlama gelir:
- 200: Basarili
- 404: Bulunamadi
- 500: Server hatasi
try/except ile hata yakalama.
Ornek kod yaz.
```

---

# HAFTA 3: Kivy Temelleri

## Gorev 3.1: Kivy Nedir?

### Prompt:
```
Kivy nedir?
Mobil uygulama gelistirmek icin nasil kullanilir?
Neden Kivy sectik? (Python-only kural)
Kisa aciklama ver.
```

---

## Gorev 3.2: Kivy Kurulumu

### Prompt:
```
Windows'ta Kivy nasil kurulur?
pip komutu ver.
Kurulumu dogrulama kodu yaz.
```

---

## Gorev 3.3: Temel Widget'lar

### Prompt:
```
Kivy'de temel widget'lar nelerdir?
Label, Button, TextInput
Her biri icin basit ornek kod yaz.
Widget'a veri nasil baglanir?
```

---

## Gorev 3.4: Event Handling

### Prompt:
```
Kivy'de event handling nedir?
Buton tiklaninca fonksiyon calistirma.
on_press ve on_release farki.
Ornek: Buton tiklaninca ekrana "Tiklandi!" yazdir.
Kod yaz.
```

### Ornek Kod:
```python
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        btn = Button(text='Tikla')
        btn.bind(on_press=self.buton_tiklandi)
        return btn
    
    def buton_tiklandi(self, instance):
        print("Buton tiklandi!")

MyApp().run()
```

---

## Gorev 3.5: Kisi 3 ile Koordinasyon

### Prompt:
```
Kisi 3 UI tasariyor, ben API baglantisi yapacagim.
Nasil koordineli calisiriz?
Ortak kod yapisi nasil olmali?
Dosya organizasyonu onerisi ver.
```

---

# HAFTA 4: Kivy ile HTTP Istekleri

## Gorev 4.1: UrlRequest Nedir?

### Prompt:
```
Kivy'de UrlRequest nedir?
requests kutuphanesinden farki ne?
Neden Kivy'de UrlRequest kullaniyoruz?
(Asenkron calisma, UI donmaz)
Acikla.
```

---

## Gorev 4.2: GET Istegi (UrlRequest)

### Prompt:
```
Kivy UrlRequest ile GET istegi yap.
from kivy.network.urlrequest import UrlRequest
API: http://localhost:5000/api/machines
Basarili response'u ekrana yazdir.
Ornek kod yaz.
```

### Ornek Kod:
```python
from kivy.network.urlrequest import UrlRequest

def on_success(req, result):
    print("Basarili:", result)

def on_error(req, error):
    print("Hata:", error)

def get_machines():
    UrlRequest(
        'http://localhost:5000/api/machines',
        on_success=on_success,
        on_error=on_error
    )
```

---

## Gorev 4.3: POST Istegi (UrlRequest)

### Prompt:
```
Kivy UrlRequest ile POST istegi yap.
API: http://localhost:5000/api/queue
Body: {"machine_id": 1, "student_id": "123"}
JSON olarak gonder.
Headers nasil eklenir?
Ornek kod yaz.
```

---

## Gorev 4.4: Response Parse Etme

### Prompt:
```
UrlRequest'ten gelen JSON response nasil parse edilir?
result parametresi zaten dictionary mi?
Icerisindeki verilere nasil erisirim?
Ornek:
result = {"machines": [{"id": 1, "name": "Makine 1"}]}
result["machines"][0]["name"] nasil alirim?
```

---

## Gorev 4.5: Hata Handle Etme

### Prompt:
```
Kivy UrlRequest'te hata durumlarini handle et.
on_error: Network hatasi
on_failure: HTTP hata kodu (404, 500)
Her durumda kullaniciya mesaj goster.
Ornek kod yaz.
```

---

# HAFTA 5: Makine Verisi Entegrasyonu

## Gorev 5.1: API Service Sinifi

### Prompt:
```
API isteklerini yoneten bir sinif yaz.
Dosya: services/api_service.py
Metodlar:
- get_machines() -> makine listesi
- get_machine(id) -> tek makine
- update_machine_status(id, status)
Kivy UrlRequest kullan.
Callback fonksiyonlari parametre olarak al.
```

---

## Gorev 5.2: Makine Listesini Cekme

### Prompt:
```
Backend'den makine listesini cek.
API: GET /api/machines
Response'u Kisi 3'un machine_card komponentine bagla.
Her makine icin bir kart olustur.
Ornek kod yaz.
```

---

## Gorev 5.3: UI'a Veri Baglama

### Prompt:
```
API'den gelen veriyi Kivy UI'a nasil baglarim?
Kisi 3'un tasarladigi MachineCard var.
for dongusuyle her makine icin kart olustur.
Kart listesini ScrollView'a ekle.
Ornek kod yaz.
```

---

## Gorev 5.4: Otomatik Yenileme

### Prompt:
```
Kivy'de periyodik gorev nasil calistirilir?
Clock.schedule_interval kullanimi.
Her 5 saniyede API'yi cagir.
Yeni veriyle UI'i guncelle.
Ornek kod yaz.
```

### Ornek Kod:
```python
from kivy.clock import Clock

class MachineListScreen(Screen):
    def on_enter(self):
        # Ekrana girince basla
        self.refresh_event = Clock.schedule_interval(self.refresh_data, 5)
    
    def on_leave(self):
        # Ekrandan cikinca durdur
        self.refresh_event.cancel()
    
    def refresh_data(self, dt):
        # API'yi cagir
        api_service.get_machines(callback=self.update_ui)
```

---

## Gorev 5.5: Cevrimdisi Durumu

### Prompt:
```
Internet baglantisi yoksa ne yapilmali?
Kullaniciya "Baglanti yok" mesaji goster.
Son bilinen veriyi goster (cache).
Tekrar dene butonu ekle.
Ornek kod yaz.
```

---

# HAFTA 6: State Yonetimi

## Gorev 6.1: State Nedir?

### Prompt:
```
Mobil uygulamada state (durum) nedir?
Neden yonetmemiz gerekir?
Ornekler:
- Yukleniyor durumu
- Hata durumu
- Veri yuklendi durumu
Basit acikla.
```

---

## Gorev 6.2: App State Sinifi

### Prompt:
```
Uygulama state'ini yoneten sinif yaz.
Dosya: services/app_state.py
Icerik:
- machines listesi
- current_user
- is_loading
- error_message
Singleton pattern kullan (tek instance).
```

---

## Gorev 6.3: Veri Cache'leme

### Prompt:
```
API'den gelen veriyi nasil cache'lerim?
Basit cache: class degiskeni olarak tut.
Gelismis: JSON dosyasina kaydet.
Cache ne zaman gecersiz olur?
Ornek kod yaz.
```

---

## Gorev 6.4: Loading Durumu

### Prompt:
```
API istegi sirasinda loading durumunu yonet.
Adimlar:
1. Istek baslamadan: is_loading = True
2. UI'da spinner goster
3. Istek bitince: is_loading = False
4. Spinner'i gizle, veriyi goster
Kisi 3'un spinner'iyla nasil entegre ederim?
```

---

## Gorev 6.5: Hata Mesajlari

### Prompt:
```
Kullaniciya hata mesaji gosterme.
Farkli hata turleri:
- Network hatasi: "Internet baglantinizi kontrol edin"
- 404: "Veri bulunamadi"
- 500: "Sunucu hatasi, daha sonra deneyin"
Kivy'de Snackbar veya Dialog ile gosterme.
Ornek kod yaz.
```

---

## Gorev 6.6: Kisi 3 ile Entegrasyon Testi

### Prompt:
```
Kisi 3'un UI'iyla benim API kodumu nasil test ederim?
Test senaryolari:
1. Makine listesi yukleniyor
2. Liste gosteriliyor
3. Hata durumu gosteriliyor
4. Otomatik yenileme calisiyor
Kontrol listesi olustur.
```

---

# HAFTA 7: Sira Sistemi Entegrasyonu

## Gorev 7.1: Siraya Girme Fonksiyonu

### Prompt:
```
Siraya girme API fonksiyonu yaz.
API: POST /api/queue
Body: {"machine_id": 1, "student_id": "2021123456"}
Basarili response: Sira bilgisi
Hata: Zaten sirada, makine yok vs.
Callback ile UI'a bildir.
```

---

## Gorev 7.2: Sira Durumu Sorgulama

### Prompt:
```
Kullanicinin sira durumunu sorgula.
API: GET /api/queue/my?student_id=2021123456
Response: Sirada mi, kacinci sirada, hangi makine
UI'da goster: "Siraniz: 3, Tahmini bekleme: 15 dk"
Ornek kod yaz.
```

---

## Gorev 7.3: Siradan Cikma

### Prompt:
```
Siradan cikma fonksiyonu yaz.
API: DELETE /api/queue/{id}
Onay dialogu goster: "Siradan cikmak istiyor musunuz?"
Basarili olunca UI'i guncelle.
Ornek kod yaz.
```

---

## Gorev 7.4: UI Baglantisi

### Prompt:
```
Kisi 3'un sira ekranina API fonksiyonlarini bagla.
Butonlar:
- "Siraya Gir" -> join_queue()
- "Iptal Et" -> leave_queue()
Kisi 3'e hangi callback'leri vermem lazim?
Ornek entegrasyon kodu yaz.
```

---

## Gorev 7.5: Bildirim Gosterimi

### Prompt:
```
Sira gelince kullaniciya bildirim goster.
Simdilik: Uygulama ici popup/dialog.
(Push notification ileride eklenebilir)
"Siraniz geldi! Makine 1 bos." mesaji.
Kivy'de nasil yaparim?
```

---

# HAFTA 8: Test ve Hata Duzeltme

## Gorev 8.1: API Test Senaryolari

### Prompt:
```
Mobil uygulama API entegrasyonu test senaryolari yaz.
Test edilecekler:
1. Makine listesi basariyla yukleniyor
2. Tek makine detayi geliyor
3. Siraya girme calisiyor
4. Siradan cikma calisiyor
5. Hata durumlarinda uygun mesaj
Her senaryo icin beklenen sonuc yaz.
```

---

## Gorev 8.2: Hata Senaryolari Testi

### Prompt:
```
Hata senaryolarini nasil test ederim?
1. Backend kapali -> Network error
2. Yanlis endpoint -> 404
3. Gecersiz veri -> 400
4. Server hatasi -> 500
Her durumda uygulama crash olmamali.
Test adimlari yaz.
```

---

## Gorev 8.3: Performans

### Prompt:
```
Kivy uygulamasinda performans nasil olculur?
Dikkat edilecekler:
- API istekleri UI'i donduruyor mu?
- Memory leak var mi?
- Liste cok uzunsa kayma akici mi?
Iyilestirme onerileri ver.
```

---

## Gorev 8.4: Demo Kontrol Listesi

### Prompt:
```
Demo oncesi kontrol listesi olustur.
API Entegrasyonu:
[ ] Backend calisir durumda mi?
[ ] Makine listesi yukleniyor mu?
[ ] Durum renkleri dogru mu?
[ ] Otomatik yenileme calisiyor mu?
[ ] Sira sistemi calisiyor mu?
[ ] Hata mesajlari duzgun mu?
```

---

# SIK KARSILASILAN HATALAR

## Hata 1: UrlRequest Calismadi
```
Prompt: "Kivy UrlRequest calismadi, on_success tetiklenmiyor.
Kod:
UrlRequest('http://localhost:5000/api/machines', on_success=self.success)
Hata mesaji yok, hic bir sey olmuyor.
Neden olabilir?"
```

## Hata 2: JSON Parse Hatasi
```
Prompt: "API'den gelen veri parse edilemiyor.
Hata: 'str' object has no attribute 'get'
result zaten string mi geliyor?
json.loads() kullanmam mi lazim?"
```

## Hata 3: UI Guncellenmiyor
```
Prompt: "API'den veri geldi ama ekran guncellenmiyor.
print(result) calisiyor, veri var.
Ama Label.text degismiyor.
Kivy'de UI main thread'de mi guncellemem lazim?"
```

## Hata 4: Connection Refused
```
Prompt: "UrlRequest 'Connection refused' hatasi veriyor.
Backend http://localhost:5000'de calisiyor.
Postman ile istek atinca calisiyor.
Kivy'den neden olmuyor?"
```

## Hata 5: Timeout
```
Prompt: "API istegi cok uzun suruyor, timeout oluyor.
UrlRequest'te timeout nasil ayarlanir?
Default timeout kac saniye?
Timeout olunca kullaniciya ne gostermeliyim?"
```

---

# DEBUGGING IPUCLARI

```
Prompt: "Kivy uygulamasinda API debugging nasil yapilir?
1. Request URL'ini logla
2. Request body'i logla
3. Response'u logla
4. Hata detaylarini logla
Logger kullanimi ornegi ver."
```

---

# YARDIM ISTEME SABLONU

Takildiginda su formati kullan:

```
SORUN: [Ne yapmaya calisiyorsun]
HATA: [Tam hata mesaji]
DENEDIKLERIM: [Simdiye kadar ne denedin]
ORTAM: Python 3.12, Kivy 2.x, Windows
API ENDPOINT: [Hangi API'yi cagiriyorsun]
REQUEST: [Gonderdigin veri]
RESPONSE: [Gelen veri veya hata]
KOD: [Ilgili kod parcasi]
```

---

**Basarilar!**
