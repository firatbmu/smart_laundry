import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routes import machines, queue
from services.mqtt_handler import start_mqtt_listener

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ── Startup ──────────────────────────────────────────────────────────────
    logger.info("Tablolar oluşturuluyor...")
    Base.metadata.create_all(bind=engine)

    logger.info("MQTT listener başlatılıyor...")
    start_mqtt_listener()

    yield
    # ── Shutdown (gerekirse cleanup buraya) ──────────────────────────────────


app = FastAPI(
    title="Smart Laundry API",
    description="Yurt çamaşırhanesi makine takip sistemi",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Production'da mobil app origin'iyle sınırla
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(machines.router)
app.include_router(queue.router)


@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "message": "Smart Laundry API çalışıyor"}
