from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import Machine, VALID_STATUSES

router = APIRouter(prefix="/api/machines", tags=["machines"])


class StatusUpdate(BaseModel):
    status: str


@router.get("")
def get_machines(db: Session = Depends(get_db)):
    """Tüm makinelerin listesini döndür."""
    machines = db.query(Machine).order_by(Machine.id).all()
    return {"machines": [m.to_dict() for m in machines]}


@router.get("/{machine_id}")
def get_machine(machine_id: int, db: Session = Depends(get_db)):
    """Belirtilen ID'li makineyi döndür."""
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Makine bulunamadı")
    return machine.to_dict()


@router.put("/{machine_id}/status")
def update_status(
    machine_id: int,
    body: StatusUpdate,
    db: Session = Depends(get_db),
):
    """Makinenin durumunu manuel güncelle."""
    if body.status not in VALID_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"Geçersiz status. Kabul edilenler: {sorted(VALID_STATUSES)}",
        )
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Makine bulunamadı")

    machine.status = body.status
    machine.last_update = datetime.utcnow()
    db.commit()
    db.refresh(machine)
    return machine.to_dict()
