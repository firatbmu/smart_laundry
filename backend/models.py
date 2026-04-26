from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

VALID_STATUSES = {"AVAILABLE", "RUNNING", "FINISHING", "FINISHED"}


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    status = Column(String(20), default="AVAILABLE", nullable=False)
    esp_device_id = Column(String(50), unique=True, nullable=False)
    last_update = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    queue_entries = relationship("Queue", back_populates="machine", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "esp_device_id": self.esp_device_id,
            "last_update": self.last_update.isoformat() if self.last_update else None,
        }


class Queue(Base):
    __tablename__ = "queue"

    id = Column(Integer, primary_key=True, autoincrement=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    student_id = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # WAITING -> NOTIFIED -> COMPLETED | CANCELLED | EXPIRED
    status = Column(String(20), default="WAITING", nullable=False)

    machine = relationship("Machine", back_populates="queue_entries")

    def to_dict(self, position: int | None = None):
        data = {
            "id": self.id,
            "machine_id": self.machine_id,
            "student_id": self.student_id,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }
        if position is not None:
            data["position"] = position
        return data
