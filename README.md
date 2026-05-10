# 🧺 Smart Laundry - Akıllı Çamaşırhane Takip Sistemi

Yurt çamaşırhanelerindeki makinelerin durumunu gerçek zamanlı takip eden IoT tabanlı sistem.

## 🎯 Proje Özeti

Öğrenciler, mobil uygulama üzerinden çamaşır makinelerinin durumunu (boş/dolu/bitti) anlık olarak görebilir ve gerektiğinde sıraya girebilir.

## 🏗️ System Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    WASHING      │     │     ESP32 +     │     │     MQTT        │
│    MACHINE      │────▶│    ADXL345      │────▶│    BROKER      │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
                                               ┌─────────────────┐
                                               │  FASTAPI BACKEND│
                                               │  + SQLite DB    │
                                               └────────┬────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │  MOBİL UYGULAMA │
                                               │  (Kivy/KivyMD)  │
                                               └─────────────────┘
```






