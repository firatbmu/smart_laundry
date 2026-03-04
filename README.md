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
| **Kişi 1** | IoT/Hardware| [📖 Rehber](docs/rehberler/ai_rehberi_kisi1_iot.md) |
| **Kişi 2** | Backend Developer | [📖 Rehber](docs/rehberler/ai_rehberi_kisi2_backend.md) |
| **Kişi 3** | Mobile Developer - UI/UX | [📖 Rehber](docs/rehberler/ai_rehberi_kisi3_ui.md) |
| **Kişi 4** | Mobile Developer - Entegrasyon | [📖 Rehber](docs/rehberler/ai_rehberi_kisi4_entegrasyon.md) |
| **Kişi 5** | QA Engineer & Documentation | [📖 Rehber](docs/rehberler/ai_rehberi_kisi5_qa.md) |

