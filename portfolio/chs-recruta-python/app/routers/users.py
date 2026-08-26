from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Role, User
from ..security import admin_user, hash_password

router = APIRouter(prefix="/api/users", tags=["users"])


class UserCreate(BaseModel):
    username: str = Field(min_length=2, max_length=80)
    display_name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8, max_length=200)
    role: Role = Role.recruiter


@router.get("")
def list_users(_: User = Depends(admin_user), db: Session = Depends(get_db)):
    users = db.scalars(select(User).order_by(User.display_name)).all()
    return [
        {
            "id": user.id,
            "username": user.username,
            "display_name": user.display_name,
            "email": user.email,
            "role": user.role.value,
            "active": user.active,
        }
        for user in users
    ]


@router.post("", status_code=201)
def create_user(payload: UserCreate, _: User = Depends(admin_user), db: Session = Depends(get_db)):
    existing = db.scalar(select(User).where(or_(User.username == payload.username, User.email == str(payload.email))))
    if existing:
        raise HTTPException(status_code=409, detail="Usuário ou e-mail já cadastrado")
    user = User(
        username=payload.username,
        display_name=payload.display_name,
        email=str(payload.email),
        password_hash=hash_password(payload.password),
        role=payload.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "id": user.id,
        "username": user.username,
        "display_name": user.display_name,
        "email": user.email,
        "role": user.role.value,
        "active": user.active,
    }
