from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Vacancy
from ..schemas import VacancyCreate, VacancyRead
from ..services import audit, normalize_profession

router = APIRouter(prefix="/api/vacancies", tags=["vacancies"])


@router.get("", response_model=list[VacancyRead])
def list_vacancies(db: Session = Depends(get_db)):
    return db.scalars(select(Vacancy).order_by(Vacancy.created_at.desc())).all()


@router.post("", response_model=VacancyRead, status_code=201)
def create_vacancy(payload: VacancyCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    data["profession"] = normalize_profession(payload.profession)
    vacancy = Vacancy(**data)
    db.add(vacancy)
    db.flush()
    audit(db, action="create", entity="vacancy", entity_id=str(vacancy.id), details=vacancy.code)
    db.commit()
    db.refresh(vacancy)
    return vacancy


@router.put("/{vacancy_id}", response_model=VacancyRead)
def update_vacancy(vacancy_id: int, payload: VacancyCreate, db: Session = Depends(get_db)):
    vacancy = db.get(Vacancy, vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")
    data = payload.model_dump()
    data["profession"] = normalize_profession(payload.profession)
    for key, value in data.items():
        setattr(vacancy, key, value)
    audit(db, action="update", entity="vacancy", entity_id=str(vacancy.id), details=vacancy.code)
    db.commit()
    db.refresh(vacancy)
    return vacancy
