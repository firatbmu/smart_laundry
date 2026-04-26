import requests

BASE_URL = "http://localhost:8000"


def get_machines():
    """Tüm makineleri döndür. Hata durumunda boş liste."""
    try:
        resp = requests.get(f"{BASE_URL}/api/machines", timeout=5)
        resp.raise_for_status()
        return resp.json().get("machines", [])
    except requests.RequestException:
        return []


def get_machine(machine_id):
    """Tek bir makineyi döndür. Hata durumunda None."""
    try:
        resp = requests.get(f"{BASE_URL}/api/machines/{machine_id}", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException:
        return None


def join_queue(machine_id, student_id):
    """Sıraya gir. Başarıda sıra dict'i, hata durumunda (None, hata_mesajı)."""
    try:
        resp = requests.post(
            f"{BASE_URL}/api/queue",
            json={"machine_id": machine_id, "student_id": student_id},
            timeout=5,
        )
        if resp.status_code == 201:
            return resp.json(), None
        return None, resp.json().get("detail", "Bilinmeyen hata")
    except requests.RequestException as e:
        return None, str(e)


def get_machine_queue(machine_id):
    """Bir makinenin sırasını döndür. Hata durumunda boş liste."""
    try:
        resp = requests.get(f"{BASE_URL}/api/queue/machine/{machine_id}", timeout=5)
        resp.raise_for_status()
        return resp.json().get("queue", [])
    except requests.RequestException:
        return []


def leave_queue(queue_id, student_id):
    """Sıradan çık. Başarıda True, hata durumunda (False, hata_mesajı)."""
    try:
        resp = requests.delete(
            f"{BASE_URL}/api/queue/{queue_id}",
            params={"student_id": student_id},
            timeout=5,
        )
        if resp.status_code == 200:
            return True, None
        return False, resp.json().get("detail", "Bilinmeyen hata")
    except requests.RequestException as e:
        return False, str(e)
