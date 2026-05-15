from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import Machine, Queue

router = APIRouter(prefix="/api/queue", tags=["queue"])


class QueueCreate(BaseModel):
    machine_id: int
    student_id: str


@router.get("/my")
def get_my_queue(machine_id: int, tc: str, db: Session = Depends(get_db)):
    """Kullanıcının belirli bir makine için aktif sıra kaydını ve pozisyonunu döndür."""
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Makine bulunamadı")

    entry = db.query(Queue).filter(
        Queue.machine_id == machine_id,
        Queue.student_id == tc,
        Queue.status == "WAITING",
    ).first()

    if not entry:
        return {"entry": None, "position": None}

    position = (
        db.query(Queue)
        .filter(
            Queue.machine_id == machine_id,
            Queue.status == "WAITING",
            Queue.created_at <= entry.created_at,
        )
        .count()
    )
    return {"entry": entry.to_dict(position=position), "position": position}


@router.post("", status_code=201)
def join_queue(body: QueueCreate, db: Session = Depends(get_db)):
    """Belirtilen makine için sıraya gir."""
    machine = db.query(Machine).filter(Machine.id == body.machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Makine bulunamadı")

    # Aynı öğrenci, aynı makine için zaten WAITING'deyse engelle
    already_waiting = db.query(Queue).filter(
        Queue.machine_id == body.machine_id,
        Queue.student_id == body.student_id,
        Queue.status == "WAITING",
    ).first()
    if already_waiting:
        raise HTTPException(
            status_code=400,
            detail="You are already in the queue for this machine",
        )

    entry = Queue(machine_id=body.machine_id, student_id=body.student_id)
    db.add(entry)
    db.commit()
    db.refresh(entry)

    # Kaydedilen girişin sıradaki pozisyonu
    position = (
        db.query(Queue)
        .filter(Queue.machine_id == body.machine_id, Queue.status == "WAITING")
        .count()
    )

    return entry.to_dict(position=position)


@router.get("/machine/{machine_id}")
def get_machine_queue(machine_id: int, db: Session = Depends(get_db)):
    """Bir makinenin WAITING sırasını listele (en eski → en yeni)."""
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Makine bulunamadı")

    entries = (
        db.query(Queue)
        .filter(Queue.machine_id == machine_id, Queue.status == "WAITING")
        .order_by(Queue.created_at)
        .all()
    )

    return {
        "machine_id": machine_id,
        "machine_name": machine.name,
        "queue": [e.to_dict(position=i + 1) for i, e in enumerate(entries)],
    }


@router.delete("/{queue_id}")
def leave_queue(
    queue_id: int,
    student_id: str = Query(..., description="National ID of the user cancelling"),
    db: Session = Depends(get_db),
):
    """Cancel a queue entry (only the owner can cancel their own entry)."""
    entry = db.query(Queue).filter(Queue.id == queue_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Sıra kaydı bulunamadı")
    if entry.student_id != student_id:
        raise HTTPException(
            status_code=403,
            detail="Bu kaydı iptal etme yetkiniz yok",
        )
    if entry.status != "WAITING":
        raise HTTPException(
            status_code=400,
            detail=f"Sadece WAITING durumundaki kayıtlar iptal edilebilir (mevcut: {entry.status})",
        )

    entry.status = "CANCELLED"
    db.commit()
    return {"message": "Sıra iptal edildi", "id": queue_id}
