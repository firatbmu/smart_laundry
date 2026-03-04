# AI Kullanim Rehberi - Kisi 3 (Mobile Developer - UI/UX)

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

## Gorev 1.2: Degiskenler ve Veri Tipleri

### Prompt:
```
Python'da degiskenler nasil tanimlanir?
Veri tipleri nelerdir:
- string (metin)
- integer (tam sayi)
- float (ondalik)
- boolean (True/False)
- list (liste)
Her biri icin ornek kod yaz.
```

---

## Gorev 1.3: Listeler

### Prompt:
```
Python'da liste (list) nasil kullanilir?
Ornekler:
- Liste olusturma
- Eleman ekleme (append)
- Eleman silme (remove)
- Listeyi donme (for dongusu)
- Liste uzunlugu (len)
Kod ornekleriyle anlat.
```

---

## Gorev 1.4: Donguler

### Prompt:
```
Python'da donguler nasil kullanilir?
for dongusu ornekleri:
- Liste uzerinde donme
- range() ile sayma
- enumerate() ile index alma
while dongusu ornegi
break ve continue ne ise yarar?
```

---

## Gorev 1.5: Fonksiyonlar

### Prompt:
```
Python'da fonksiyon nasil yazilir?
def anahtar kelimesi
Parametre alma
Deger dondurme (return)
Varsayilan parametre
Ornekler:
- Toplama fonksiyonu
- Selam veren fonksiyon
- Liste ortalaması hesaplayan fonksiyon
```

---

## Gorev 1.6: Siniflar (Class)

### Prompt:
```
Python'da class (sinif) nedir?
__init__ metodu ne ise yarar?
self ne demek?
Basit bir sinif ornegi:
- Ogrenci sinifi
- Ozellikler: isim, numara
- Metod: bilgileri yazdir
```

---

# HAFTA 2: Kivy Temelleri

## Gorev 2.1: Kivy Nedir?

### Prompt:
```
Kivy nedir?
Ne icin kullanilir?
Hangi platformlarda calisir?
Neden mobil uygulama icin Kivy sectik?
Kisa ve oz anlat.
```

---

## Gorev 2.2: Kivy ve KivyMD Kurulumu

### Prompt:
```
Windows'ta Kivy ve KivyMD nasil kurulur?
pip komutlarini ver.
Kurulumu dogrulama kodu yaz.
Olasi hatalar ve cozumleri.
```

### Beklenen Komutlar:
```bash
pip install kivy
pip install kivymd
```

---

## Gorev 2.3: Ilk Kivy Uygulamasi

### Prompt:
```
Kivy ile "Hello World" uygulamasi yaz.
Ekranda "Merhaba Dunya" yazan bir Label olsun.
Pencere boyutu: 360x640 (telefon boyutu)
Kodu yaz ve nasil calistirilacagini anlat.
```

### Beklenen Kod:
```python
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Merhaba Dunya')

if __name__ == '__main__':
    MyApp().run()
```

---

## Gorev 2.4: Widget Kavrami

### Prompt:
```
Kivy'de widget nedir?
Temel widget'lar:
- Label (yazi)
- Button (buton)
- TextInput (metin girisi)
- Image (resim)
Her biri icin basit ornek kod yaz.
```

---

## Gorev 2.5: Layout'lar

### Prompt:
```
Kivy'de layout nedir?
Temel layout'lar:
- BoxLayout (yatay/dikey siralama)
- GridLayout (izgara)
- FloatLayout (serbest konumlama)
BoxLayout ile 3 buton alt alta siralama ornegi yaz.
```

---

## Gorev 2.6: .kv Dosyasi

### Prompt:
```
Kivy'de .kv dosyasi nedir?
Python kodundan ayri tasarim dosyasi.
Avantajlari neler?
Sozdizimi nasil?
Ornek: main.py + main.kv ayri dosyalarda ayni uygulama.
```

### Ornek main.kv:
```kv
BoxLayout:
    orientation: 'vertical'
    
    Label:
        text: 'Merhaba'
    
    Button:
        text: 'Tikla'
```

---

# HAFTA 3: KivyMD Material Design

## Gorev 3.1: KivyMD Nedir?

### Prompt:
```
KivyMD nedir?
Material Design ne demek?
Kivy'den farki ne?
Neden KivyMD kullaniyoruz?
```

---

## Gorev 3.2: KivyMD Baslangic

### Prompt:
```
KivyMD ile basit uygulama yaz.
MDApp sinifini kullan.
Tema rengi ayarla (mavi).
"Akilli Camasirhane" baslikli ekran.
```

### Beklenen Kod:
```python
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

class LaundryApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()
        screen.add_widget(MDLabel(
            text="Akilli Camasirhane",
            halign="center"
        ))
        return screen

LaundryApp().run()
```

---

## Gorev 3.3: MDCard

### Prompt:
```
KivyMD'de MDCard nedir?
Nasil kullanilir?
Icerisine Label ve Button nasil eklenir?
Golge efekti (elevation) nasil ayarlanir?
Ornek kod yaz.
```

---

## Gorev 3.4: MDLabel ve MDButton

### Prompt:
```
KivyMD'de MDLabel kullanimi.
Font boyutu, renk, hizalama nasil ayarlanir?
MDRaisedButton ve MDFlatButton farki.
Buton rengi nasil degistirilir?
Buton tiklandiginda fonksiyon calistirma.
Ornekler ver.
```

---

## Gorev 3.5: MDToolbar

### Prompt:
```
KivyMD'de MDToolbar nedir?
Ust menu cubugu nasil eklenir?
Baslik nasil yazilir?
Sol ve sag tarafina ikon nasil eklenir?
Ornek kod yaz.
```

---

## Gorev 3.6: Renk Temasi

### Prompt:
```
KivyMD'de tema renkleri nasil ayarlanir?
theme_cls.primary_palette
theme_cls.accent_palette
Mevcut renk paletleri neler?
Koyu/acik tema nasil degistirilir?
Uygulamamiz icin uygun renk secimi yap:
- Ana renk: Mavi (temizlik/su cagrisimlari)
- Vurgu renk: Yesil (musait) veya Turuncu (mesgul)
```

---

# HAFTA 4: Ana Ekran Tasarimi

## Gorev 4.1: Ekran Yapisi

### Prompt:
```
KivyMD ile ana ekran (home screen) olustur.
Dosya: screens/home.py
Icerik:
- Ust toolbar: "Camasirhane" basligi
- Ortada: Hosgeldin mesaji
- Altta: 2 buton (Makineler, Siram)
Kodu yaz.
```

---

## Gorev 4.2: MDScreen Kullanimi

### Prompt:
```
KivyMD'de MDScreen nedir?
Screen'e isim nasil verilir?
Screen icerisine widget nasil eklenir?
home.kv dosyasi nasil yazilir?
Ornek ver.
```

---

## Gorev 4.3: Navigasyon Butonlari

### Prompt:
```
Ana ekranda 2 buton tasarla.
Buton 1: "Makine Durumu" - mavi, buyuk
Buton 2: "Sirama Bak" - yesil, buyuk
Butonlar yan yana veya alt alta olsun.
Buton tiklaninca ekran degistirme (simdilik print).
Kodu yaz.
```

---

## Gorev 4.4: Ikon Kullanimi

### Prompt:
```
KivyMD'de ikon nasil kullanilir?
MDIconButton nedir?
Mevcut ikonlar nereden bulunur? (Material Design Icons)
"washing-machine" ve "account-clock" ikonlarini kullan.
Ornek kod yaz.
```

---

## Gorev 4.5: Uygulama Ikonu

### Prompt:
```
Kivy uygulamasina ikon nasil eklenir?
Pencere basligi nasil degistirilir?
icon.png dosyasi nasil kullanilir?
Kodu goster.
```

---

# HAFTA 5: Makine Listesi Ekrani

## Gorev 5.1: ScrollView

### Prompt:
```
KivyMD'de ScrollView nasil kullanilir?
Cok sayida eleman oldugunda kaydirilabilir liste.
MDList icinde MDCard'lar.
Ornek kod yaz.
```

---

## Gorev 5.2: machine_list.py Ekrani

### Prompt:
```
Makine listesi ekrani olustur.
Dosya: screens/machine_list.py
Icerik:
- Toolbar: "Makineler" basligi + geri butonu
- Liste: 3 makine karti (simdilik statik veri)
Her kart:
- Makine adi
- Durum (AVAILABLE/RUNNING/FINISHED)
- Son guncelleme
Kodu yaz.
```

---

## Gorev 5.3: machine_card.py Komponenti

### Prompt:
```
Makine karti komponenti olustur.
Dosya: components/machine_card.py
MDCard icinde:
- Sol: Makine ikonu (washing-machine)
- Orta: Makine adi + durum
- Sag: Durum rengi (yesil/turuncu/gri daire)
Kodu yaz, yeniden kullanilabilir olsun.
```

---

## Gorev 5.4: Durum Renkleri

### Prompt:
```
Makine durumuna gore renk goster.
AVAILABLE -> Yesil (#4CAF50)
RUNNING -> Turuncu (#FF9800)
FINISHED -> Gri (#9E9E9E)
KivyMD'de dinamik renk degistirme nasil yapilir?
Ornek kod yaz.
```

---

## Gorev 5.5: Responsive Tasarim

### Prompt:
```
Kivy'de responsive tasarim nasil yapilir?
Ekran boyutuna gore widget boyutlandirma.
size_hint kullanimi.
dp (density-independent pixels) nedir?
Telefon ekranina uygun tasarim ornegi.
```

---

## Gorev 5.6: Zaman Formatlama

### Prompt:
```
Python'da tarih/saat nasil formatlanir?
datetime modulu kullanimi.
"2024-01-15T14:30:00" -> "15 Ocak, 14:30" formatina cevirme.
"5 dakika once", "1 saat once" gosterimi.
Ornek kod yaz.
```

---

# HAFTA 6: Ekran Gecisleri

## Gorev 6.1: ScreenManager

### Prompt:
```
Kivy'de ScreenManager nedir?
Birden fazla ekran arasinda gecis.
Ekran isimleri ve gecis metodlari.
Ornek: HomeScreen ve MachineListScreen arasi gecis.
Kodu yaz.
```

---

## Gorev 6.2: Gecis Animasyonlari

### Prompt:
```
Kivy ScreenManager'da gecis animasyonlari.
Mevcut transition tipleri:
- SlideTransition
- FadeTransition
- SwapTransition
Sola/saga kayma animasyonu nasil ayarlanir?
Ornek kod yaz.
```

---

## Gorev 6.3: Bottom Navigation

### Prompt:
```
KivyMD'de MDBottomNavigation nasil kullanilir?
Alt menu cubugu olustur.
3 sekme:
- Ana Sayfa (home ikonu)
- Makineler (washing-machine ikonu)
- Profilim (account ikonu)
Sekme tiklaninca ekran degissin.
Kodu yaz.
```

---

## Gorev 6.4: Geri Butonu

### Prompt:
```
KivyMD'de geri butonu nasil eklenir?
MDTopAppBar'a sol taraf ikonu.
Tiklaninca onceki ekrana don.
Android geri tusunu da handle et (on_keyboard).
Ornek kod yaz.
```

---

## Gorev 6.5: Loading Gostergesi

### Prompt:
```
KivyMD'de loading (yukleniyor) gostergesi nasil eklenir?
MDSpinner kullanimi.
Veri yuklenirken spinner goster.
Yukleme bitince gizle.
Ornek kod yaz.
```

---

# HAFTA 7: Sira Ekrani

## Gorev 7.1: queue.py Ekrani

### Prompt:
```
Sira alma ekrani olustur.
Dosya: screens/queue.py
Icerik:
- Toolbar: "Sira Al" basligi
- Makine secimi (dropdown veya liste)
- "Siraya Gir" butonu
- Mevcut sira durumu gosterimi
Kodu yaz.
```

---

## Gorev 7.2: Form Tasarimi

### Prompt:
```
KivyMD ile form tasarla.
Icerik:
- MDDropdownMenu ile makine secimi
- MDTextField ile ogrenci numarasi (opsiyonel)
- MDRaisedButton ile "Siraya Gir"
Form validasyonu nasil yapilir?
Ornek kod yaz.
```

---

## Gorev 7.3: Sira Durumu Gosterimi

### Prompt:
```
Kullanicinin sira durumunu gosteren kart tasarla.
Icerik:
- "Siraniz: 3" buyuk yazi
- "Tahmini bekleme: ~15 dk" 
- "Iptal Et" butonu
Kart gorunur/gizli nasil yapilir?
Ornek kod yaz.
```

---

## Gorev 7.4: Onay/Iptal Butonlari

### Prompt:
```
Siraya girdikten sonra onay ekrani goster.
Dialog veya Snackbar kullan.
"Siraya eklendi!" mesaji.
"Iptal" butonu tiklaninca onay dialogu.
MDDialog kullanimi ornegi ver.
```

---

## Gorev 7.5: Kisi 4 ile Entegrasyon

### Prompt:
```
UI ekranlarini API'ye nasil baglayacagim?
Kisi 4'un yazacagi fonksiyonlar:
- get_machines() -> makine listesi
- join_queue(machine_id) -> siraya gir
- get_my_queue() -> sira durumum
Ben UI'da bu fonksiyonlari nasil cagiririm?
Callback ve event binding ornegi ver.
```

---

# HAFTA 8: Son Duzeltmeler

## Gorev 8.1: UI/UX Iyilestirmeleri

### Prompt:
```
Mobil uygulama UI/UX iyilestirme onerileri ver.
Kontrol listesi:
- Butonlar yeterince buyuk mu? (en az 48dp)
- Renkler tutarli mi?
- Bosluklar (padding/margin) duzgun mu?
- Font boyutlari okunabilir mi?
KivyMD best practices neler?
```

---

## Gorev 8.2: Hata Mesaji Ekranlari

### Prompt:
```
Kullaniciya hata mesaji gosterme yontemleri.
KivyMD ile:
- Snackbar (kisa mesaj, altta)
- Dialog (onemli uyari, popup)
- Toast (Android tarz bildirim)
Her biri icin ornek kod yaz.
```

---

## Gorev 8.3: Animasyonlar

### Prompt:
```
KivyMD'de basit animasyonlar.
Ornekler:
- Buton tiklaninca buyume efekti
- Kart acilirken fade-in
- Liste elemani eklenirken kayma
Animation sinifi kullanimi.
Ornek kod yaz.
```

---

## Gorev 8.4: Demo Hazirligi

### Prompt:
```
Mobil uygulama demosunu nasil yaparim?
Kontrol listesi:
- Tum ekranlar calisiyor mu?
- Gecisler akici mi?
- Hata durumlarinda crash olmuyor mu?
- Sahte veri mi gercek veri mi kullanilacak?
Demo senaryosu yaz.
```

---

# SIK KARSILASILAN HATALAR

## Hata 1: Kivy Penceresi Acilmiyor
```
Prompt: "Kivy uygulamasini calistirinca hic pencere acilmiyor.
Hata mesaji yok, program hemen kapaniyor.
Windows kullaniyorum.
Nasil debug ederim?"
```

## Hata 2: KivyMD Import Hatasi
```
Prompt: "'ModuleNotFoundError: No module named kivymd' hatasi aliyorum.
pip install kivymd yaptim.
Virtual environment aktif.
Neden olmuyor?"
```

## Hata 3: .kv Dosyasi Yuklenmedi
```
Prompt: "main.kv dosyami uygulama yuklemiyor.
Ekran bos geliyor.
Dosya isimleri:
- main.py
- main.kv
Nerede hata yapiyorum?"
```

## Hata 4: Widget Boyutlandirma
```
Prompt: "Butonlarim cok kucuk gorunuyor.
size_hint ve size nasil kullanilir?
dp() ne ise yarar?
Telefon ekranina uygun boyut nasil ayarlarim?"
```

## Hata 5: Renk Calismiyor
```
Prompt: "MDCard'in arka plan rengini degistiremiyorum.
md_bg_color ayarladim ama beyaz kaliyor.
KivyMD'de renk nasil verilir? RGB mi RGBA mi?"
```

---

# TASARIM ILHAM KAYNAKLARI

```
Prompt: "Camasirhane uygulamasi icin UI tasarim ilhami ver.
Renk paleti onerisi
Ikon onerileri
Ekran duzenlemesi
Modern ve minimalist olsun."
```

---

# YARDIM ISTEME SABLONU

Takildiginda su formati kullan:

```
SORUN: [Ne yapmaya calisiyorsun]
HATA: [Tam hata mesaji]
DENEDIKLERIM: [Simdiye kadar ne denedin]
ORTAM: Python 3.12, Kivy 2.x, KivyMD 1.x, Windows
KOD: [Ilgili kod parcasi]
EKRAN GORUNTUSU: [Varsa, ne gorunuyor]
```

---

**Basarilar!**
