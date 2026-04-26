"""
Backend API testleri.
Çalıştırma: cd backend && pytest tests/ -v
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# StaticPool: tüm bağlantılar aynı in-memory DB'yi paylaşır
test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# Modül-düzeyinde override (import öncesi yapılmalı)
import database as db_module
db_module.engine = test_engine
db_module.SessionLocal = TestSessionLocal

from database import Base, get_db
from main import app
from models import Machine, Queue


def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def fresh_db():
    """Her test için temiz şema."""
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def client(fresh_db):  # fresh_db'ye bağımlı → tablolar önce oluşur
    with TestClient(app, raise_server_exceptions=True) as c:
        yield c


@pytest.fixture
def db(fresh_db):
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def machine(db):
    """Test için tek makine oluşturur."""
    m = Machine(name="Test Makinesi", esp_device_id="esp32_test", status="AVAILABLE")
    db.add(m)
    db.commit()
    db.refresh(m)
    return m


# ── /api/machines ────────────────────────────────────────────────────────────

class TestGetMachines:
    def test_bos_liste(self, client):
        r = client.get("/api/machines")
        assert r.status_code == 200
        assert r.json() == {"machines": []}

    def test_makineler_listelenir(self, client, db):
        db.add_all([
            Machine(name="Makine 1", esp_device_id="esp32_001"),
            Machine(name="Makine 2", esp_device_id="esp32_002"),
        ])
        db.commit()
        r = client.get("/api/machines")
        assert r.status_code == 200
        data = r.json()["machines"]
        assert len(data) == 2
        assert all(k in data[0] for k in ("id", "name", "status", "esp_device_id", "last_update"))


class TestGetMachine:
    def test_var_olan_makine(self, client, machine):
        r = client.get(f"/api/machines/{machine.id}")
        assert r.status_code == 200
        assert r.json()["esp_device_id"] == "esp32_test"

    def test_olmayan_makine_404(self, client):
        r = client.get("/api/machines/9999")
        assert r.status_code == 404


class TestUpdateStatus:
    def test_basarili_guncelleme(self, client, machine):
        r = client.put(f"/api/machines/{machine.id}/status", json={"status": "RUNNING"})
        assert r.status_code == 200
        assert r.json()["status"] == "RUNNING"

    def test_gecersiz_status_400(self, client, machine):
        r = client.put(f"/api/machines/{machine.id}/status", json={"status": "UCUYOR"})
        assert r.status_code == 400

    def test_olmayan_makine_404(self, client):
        r = client.put("/api/machines/9999/status", json={"status": "RUNNING"})
        assert r.status_code == 404

    def test_tum_gecerli_statusler(self, client, machine):
        for status in ("AVAILABLE", "RUNNING", "FINISHING", "FINISHED"):
            r = client.put(f"/api/machines/{machine.id}/status", json={"status": status})
            assert r.status_code == 200, f"{status} geçerli olmalıydı"


# ── /api/queue ───────────────────────────────────────────────────────────────

class TestJoinQueue:
    def test_siraya_gir(self, client, machine):
        r = client.post("/api/queue", json={"machine_id": machine.id, "student_id": "2021001"})
        assert r.status_code == 201
        body = r.json()
        assert body["status"] == "WAITING"
        assert body["position"] == 1

    def test_olmayan_makine_404(self, client):
        r = client.post("/api/queue", json={"machine_id": 9999, "student_id": "2021001"})
        assert r.status_code == 404

    def test_ayni_ogrenci_iki_kez_giremez(self, client, machine):
        payload = {"machine_id": machine.id, "student_id": "2021001"}
        client.post("/api/queue", json=payload)
        r = client.post("/api/queue", json=payload)
        assert r.status_code == 400

    def test_farkli_ogrenciler_siraya_girebilir(self, client, machine):
        for i, sid in enumerate(["2021001", "2021002", "2021003"], start=1):
            r = client.post("/api/queue", json={"machine_id": machine.id, "student_id": sid})
            assert r.status_code == 201
            assert r.json()["position"] == i


class TestGetMachineQueue:
    def test_bos_sira(self, client, machine):
        r = client.get(f"/api/queue/machine/{machine.id}")
        assert r.status_code == 200
        assert r.json()["queue"] == []

    def test_sira_listelenir(self, client, machine):
        for sid in ["2021001", "2021002"]:
            client.post("/api/queue", json={"machine_id": machine.id, "student_id": sid})
        r = client.get(f"/api/queue/machine/{machine.id}")
        queue = r.json()["queue"]
        assert len(queue) == 2
        assert queue[0]["position"] == 1
        assert queue[1]["position"] == 2

    def test_olmayan_makine_404(self, client):
        r = client.get("/api/queue/machine/9999")
        assert r.status_code == 404


class TestLeaveQueue:
    def test_basarili_iptal(self, client, machine):
        entry = client.post("/api/queue", json={"machine_id": machine.id, "student_id": "2021001"}).json()
        r = client.delete(f"/api/queue/{entry['id']}?student_id=2021001")
        assert r.status_code == 200

    def test_baska_ogrenci_iptal_edemez(self, client, machine):
        entry = client.post("/api/queue", json={"machine_id": machine.id, "student_id": "2021001"}).json()
        r = client.delete(f"/api/queue/{entry['id']}?student_id=2021999")
        assert r.status_code == 403

    def test_olmayan_kayit_404(self, client):
        r = client.delete("/api/queue/9999?student_id=2021001")
        assert r.status_code == 404

    def test_iptal_edilen_sirada_gorunmez(self, client, machine):
        entry = client.post("/api/queue", json={"machine_id": machine.id, "student_id": "2021001"}).json()
        client.delete(f"/api/queue/{entry['id']}?student_id=2021001")
        r = client.get(f"/api/queue/machine/{machine.id}")
        assert r.json()["queue"] == []


# ── services/analysis.py ─────────────────────────────────────────────────────

class TestAnalysis:
    def test_hareketsiz_sifir(self):
        from services.analysis import calculate_vibration
        assert calculate_vibration(0, 0, 1) == pytest.approx(0.0, abs=0.01)

    def test_hareket_pozitif(self):
        from services.analysis import calculate_vibration
        assert calculate_vibration(1, 1, 1) > 0

    def test_detect_running(self):
        from services.analysis import detect_status
        assert detect_status([2.0, 2.5, 1.8, 2.2, 1.9]) == "RUNNING"

    def test_detect_available(self):
        from services.analysis import detect_status
        assert detect_status([0.1, 0.2, 0.15, 0.1, 0.05]) == "AVAILABLE"

    def test_detect_finishing(self):
        from services.analysis import detect_status
        assert detect_status([0.8, 0.9, 1.0, 0.7, 0.8]) == "FINISHING"

    def test_bos_gecmis(self):
        from services.analysis import detect_status
        assert detect_status([]) == "AVAILABLE"
