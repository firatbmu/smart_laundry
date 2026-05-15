# 🧺 Smart Laundry - Smart Laundry Tracking System


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
                                               │  MOBILE APP     │
                                               │  (Kivy/KivyMD)  │
                                               └─────────────────┘
```






