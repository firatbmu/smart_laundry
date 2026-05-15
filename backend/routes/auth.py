from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel, field_validator
from sqlalchemy.orm import Session

from database import get_db
from models import User

router = APIRouter(prefix="/api/auth", tags=["auth"])

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


class RegisterRequest(BaseModel):
    tc: str
    ad: str
    soyad: str
    telefon: str
    sifre: str

    @field_validator("tc")
    @classmethod
    def tc_gecerli(cls, v):
        if not v.isdigit() or len(v) != 11:
            raise ValueError("TC kimlik numarası 11 haneli rakam olmalıdır")
        return v

    @field_validator("ad", "soyad")
    @classmethod
    def bos_olamaz(cls, v):
        if not v.strip():
            raise ValueError("Bu alan boş olamaz")
        return v.strip()

    @field_validator("sifre")
    @classmethod
    def sifre_uzunluk(cls, v):
        if len(v) < 6:
            raise ValueError("Şifre en az 6 karakter olmalıdır")
        return v


class LoginRequest(BaseModel):
    tc: str
    sifre: str


@router.post("/register", status_code=201)
def register(body: RegisterRequest, db: Session = Depends(get_db)):
    """Yeni kullanıcı kaydı oluştur."""
    existing = db.query(User).filter(User.tc == body.tc).first()
    if existing:
        raise HTTPException(status_code=400, detail="Bu TC numarası zaten kayıtlı")

    user = User(
        tc=body.tc,
        ad=body.ad,
        soyad=body.soyad,
        telefon=body.telefon,
        sifre_hash=pwd_context.hash(body.sifre),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Kayıt başarılı", "user": user.to_dict()}


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    """Kayıtlı tüm kullanıcıları listele."""
    users = db.query(User).order_by(User.id).all()
    return {"users": [u.to_dict() for u in users]}


@router.post("/login")
def login(body: LoginRequest, db: Session = Depends(get_db)):
    """TC ve şifre ile giriş yap."""
    user = db.query(User).filter(User.tc == body.tc).first()
    if not user or not pwd_context.verify(body.sifre, user.sifre_hash):
        raise HTTPException(status_code=401, detail="TC numarası veya şifre hatalı")
    return {"message": "Giriş başarılı", "user": user.to_dict()}
