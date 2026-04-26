import math

import pandas as pd


def calculate_vibration(ax: float, ay: float, az: float) -> float:
    """Ham ivme değerlerinden titreşim şiddetini hesapla.

    Yerçekimi (~1g) çıkarılır; sonuç g biriminde, 0'dan küçük olamaz.
    """
    magnitude = math.sqrt(ax**2 + ay**2 + az**2)
    return max(0.0, round(magnitude - 1.0, 4))


def detect_status(vibration_history: list[float]) -> str:
    """Son N titreşim ölçümünün ortalamasına göre makine durumunu tespit et.

    Eşik (IoT kodu ile senkronize):
      - ort > 0.150 → RUNNING   (makine çalışıyor)
      - ort ≤ 0.150 → AVAILABLE (makine boş/duruyor)
    """
    if not vibration_history:
        return "AVAILABLE"

    series = pd.Series(vibration_history, dtype=float)
    avg = series.mean()

    if avg > 0.150:
        return "RUNNING"
    else:
        return "AVAILABLE"
