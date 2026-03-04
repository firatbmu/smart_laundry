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

## 👥 Takım Rehberleri

Her takım üyesi kendi AI rehberini takip eder:

| Kişi | Rol | Haftalık Rehber |
|------|-----|-----------------|
| **Kişi 1** | Backend Developer | [📖 Rehber](docs/rehberler/ai_rehberi_kisi2_backend.md) |
| **Kişi 2** | Mobile Developer - UI/UX | [📖 Rehber](docs/rehberler/ai_rehberi_kisi3_ui.md) |
| **Kişi 3** | Mobile Developer - Entegrasyon | [📖 Rehber](docs/rehberler/ai_rehberi_kisi4_entegrasyon.md) |
| **Kişi 4** | QA Engineer & Documentation | [📖 Rehber](docs/rehberler/ai_rehberi_kisi5_qa.md) |
| **Kişi 5** | IoT & Hardware |

## 👥 Kişi bazında hızlı ilerleme analizi

Kişi 1 (Backend Developer)
Durum: FastAPI + SQLite + SQLAlchemy (Machine modeli), MQTT handler, sıra sistemi (Queue modeli ve API’leri) – Hafta 7–8 bonus.Hızlı ilerleyebilir mi? EVET, Hafta 1–6 arası büyük ölçüde bağımsız.Nereye kadar? Hafta 6 sonuna kadar API + MQTT + veri analizi tarafını “dummy veri” ile geliştirebilir.Sonra ne olur? Gerçek sensör verisi ile test için Kişi 1’in MQTT veri akışı gerekir. Hafta 7–8’de sıra sistemi (Queue modeli + /api/queue endpoint’leri) bonus olarak eklenir.Örnek: 5. haftada FastAPI + Veritabanı + API + MQTT handler ile temel backend tamamen çalışır; 7. haftada sıra sistemi API’leri eklenir.
________________________________________
Kişi 2 (Mobile UI/UX)
Durum: Kivy/KivyMD ile mobil arayüz, ekran tasarımları, tema, kullanıcı deneyimi.Hızlı ilerleyebilir mi? EVET, Hafta 1–5 arası neredeyse tamamen bağımsız.Nereye kadar? Tüm ekran tasarımlarını sahte veri (hardcoded) ile tamamlayabilir.Sonra ne olur? Hafta 6’dan itibaren Kişi 4 ile entegrasyon yaparak gerçek API verisine bağlanır. Hafta 7–8’de sıra ekranı ve küçük UI düzeltmeleri eklenir.Örnek: 3. haftada tüm temel ekranların tasarımı biter, 5. haftada makine listesi ekranı sahte verilerle tam çalışır, 6. haftada gerçek API verisine geçilir.
________________________________________
Kişi 3 (Mobile Entegrasyon)
Durum: Mobil uygulamayı backend API’lerine bağlama, state yönetimi, hata/bağlantı durumları.Hızlı ilerleyebilir mi? KISITLI.Neden? Gerçek entegrasyon için Kişi 2’nin API’leri hazır olmalı; UI tarafı için Kişi 3’ün ekran yapısı ile uyumlu çalışması gerekiyor.Ne yapabilir? Hafta 1–4: Python, Kivy temelleri, HTTP/JSON, requests, UrlRequest, sahte test API’si ile denemeler. Hafta 5–6: Backend hazır olduğunda gerçek GET /api/machines entegrasyonu, otomatik yenileme, hata mesajları, loading. Hafta 7–8: Sıra sistemi entegrasyonu (/api/queue endpoint’leri) – bonus özellik.Kritik Bağımlılık: API olmadan gerçek entegrasyon yapılamaz; Kişi 4’ün tam gücü Hafta 5’ten itibaren ortaya çıkar.
________________________________________
Kişi 4 (QA & Documentation)
Durum: Testler (pytest, API testleri, entegrasyon testleri), dokümantasyon (README, kurulum rehberi, troubleshooting, sunum).Hızlı ilerleyebilir mi? KISITLI.Neden? Test yazmak için çalışan kod gerekir.Ne yapabilir? Hafta 1–2: Git, GitHub, temel pytest, README/Markdown. Hafta 3–4: İlk unit testler, basit API testleri, dokümantasyon iskeleti. Hafta 5–6: Backend API testleri (Machine + MQTT handler), entegrasyon testleri, test coverage, bug tracking. Hafta 7–8: Sıra sistemi testleri, final dokümantasyon, kurulum rehberi, troubleshooting, sunum slaytları.Kritik Bağımlılık: Test için çalışan kod gerekli.	
Kritik Bağımlılık: Test için çalışan kod gerekli.
________________________________________
Kişi 5 (IoT/Hardware)
Durum: ESP32 + MicroPython + ADXL345 sensör, MQTT ile backend’e veri gönderimi, donanım ve takım koordinasyonu.Hızlı ilerleyebilir mi? EVET, Hafta 1–4 arası büyük ölçüde bağımsız.Nereye kadar? Hafta 4 sonuna kadar (MQTT dahil) sensör + MQTT tarafını kendi başına bitirebilir.Sonra ne olur? Hafta 5–6’da gerçek veri akışını test etmek için Kişi 2’nin backend’inin hazır olması gerekir. Hafta 7–8 sıra sistemi bonus özellik; IoT tarafı için kritik değil.Örnek: 1. haftada ESP32 kurulumu + LED testi, 2. haftada WiFi, 3. haftada ADXL345’ten veri okuma, 4. haftada MQTT ile broker’a veri gönderme tamamlanabilir.





