# 🧺 Smart Laundry - Akıllı Çamaşırhane Takip Sistemi

Yurt çamaşırhanelerindeki makinelerin durumunu gerçek zamanlı takip eden IoT tabanlı sistem.

## 🎯 Proje Özeti

Öğrenciler, mobil uygulama üzerinden çamaşır makinelerinin durumunu (boş/dolu/bitti) anlık olarak görebilir ve gerektiğinde sıraya girebilir.

## 🏗️ Sistem Mimarisi

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   ÇAMAŞIR       │     │    ESP32 +      │     │     MQTT        │
│   MAKİNESİ      │────▶│    ADXL345      │────▶│    BROKER       │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
                                               ┌─────────────────┐
                                               │  FLASK BACKEND  │
                                               │  + SQLite DB    │
                                               └────────┬────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │  MOBİL UYGULAMA │
                                               │  (Kivy/KivyMD)  │
                                               └─────────────────┘
```

## 👥 Takım Rehberleri

Her takım üyesi kendi AI rehberini takip eder:

| Kişi | Rol | Haftalık Rehber |
|------|-----|-----------------|
| **Kişi 1** | IoT/Hardware & Takım Lideri | [📖 Rehber](docs/rehberler/ai_rehberi_kisi1_iot.md) |
| **Kişi 2** | Backend Developer | [📖 Rehber](docs/rehberler/ai_rehberi_kisi2_backend.md) |
| **Kişi 3** | Mobile Developer - UI/UX | [📖 Rehber](docs/rehberler/ai_rehberi_kisi3_ui.md) |
| **Kişi 4** | Mobile Developer - Entegrasyon | [📖 Rehber](docs/rehberler/ai_rehberi_kisi4_entegrasyon.md) |
| **Kişi 5** | QA Engineer & Documentation | [📖 Rehber](docs/rehberler/ai_rehberi_kisi5_qa.md) |

## 📅 Proje Takvimi

| Hafta | Odak |
|-------|------|
| 1-3 | Temel Kurulum & Öğrenme |
| 4-5 | Geliştirme & Entegrasyon |
| 6 | Temel Sistem Tamamlama |
| 7 | Bonus: Sıra Sistemi |
| 8 | Test & Sunum Hazırlığı |

## 🛠️ Teknoloji Stack

| Katman | Teknoloji |
|--------|-----------|
| **Donanım** | ESP32, ADXL345 (İvmeölçer) |
| **Firmware** | MicroPython |
| **İletişim** | MQTT (Mosquitto) |
| **Backend** | Flask, SQLAlchemy, Pandas |
| **Veritabanı** | SQLite |
| **Mobil** | Kivy, KivyMD |
| **Test** | Pytest |

## 🚀 Kurulum

### 1. Repo'yu Klonla
```bash
git clone https://github.com/firatbmu/smart_laundry.git
cd smart_laundry
```

### 2. Virtual Environment Oluştur
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

## 📁 Klasör Yapısı

```
smart_laundry/
├── backend/          # Flask API
├── mobile/           # Kivy uygulaması
├── iot/              # ESP32 MicroPython kodları
├── tests/            # Pytest testleri
├── docs/             # Dokümantasyon
│   └── rehberler/    # Takım AI rehberleri
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Özellikler

### Temel Sistem (Hafta 1-6)
- [x] ESP32 + ADXL345 sensör entegrasyonu
- [x] Titreşim tabanlı makine durumu algılama
- [x] MQTT ile gerçek zamanlı veri iletimi
- [x] Flask REST API
- [x] Mobil uygulama (makine listesi)

### Bonus: Sıra Sistemi (Hafta 7-8)
- [ ] Sıraya girme özelliği
- [ ] Sıra takibi
- [ ] Bildirim sistemi

## 📝 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

**Takım:** IPT Projesi 2026
