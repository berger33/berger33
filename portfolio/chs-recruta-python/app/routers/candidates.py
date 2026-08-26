from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Candidate, User
from ..schemas import CandidateCreate, CandidateRead
from ..security import admin_user, current_user
from ..services import audit, find_possible_duplicate, match_vacancies, normalize_profession, search_candidates

router = APIRouter(prefix="/api/candidates", tags=["candidates"])


@router.get("", response_model=list[CandidateRead])
def list_candidates(q: str = Query(default=""), _: User = Depends(current_user), db: Session = Depends(get_db)):
    return search_candidates(db, q)


@router.post("", response_model=CandidateRead, status_code=201)
def create_candidate(payload: CandidateCreate, allow_duplicate: bool = False, user: User = Depends(current_user), db: Session = Depends(get_db)):
    duplicate = find_possible_duplicate(db, name=payload.name, phone=payload.phone, registry=payload.professional_registry)
    if duplicate and not allow_duplicate:
        raise HTTPException(status_code=409, detail={"message": "Possível candidato duplicado", "candidate_id": duplicate.id})
    data = payload.model_dump()
    data["profession"] = normalize_profession(payload.profession)
    candidate = Candidate(**data)
    db.add(candidate)
    db.flush()
    audit(db, action="create", entity="candidate", entity_id=str(candidate.id), actor=user.username, details=candidate.name)
    db.commit()
    db.refresh(candidate)
    return candidate


@router.get("/{candidate_id}", response_model=CandidateRead)
def get_candidate(candidate_id: int, _: User = Depends(current_user), db: Session = Depends(get_db)):
    candidate = db.get(Candidate, candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato não encontrado")
    return candidate


@router.put("/{candidate_id}", response_model=CandidateRead)
def update_candidate(candidate_id: int, payload: CandidateCreate, user: User = Depends(current_user), db: Session = Depends(get_db)):
    candidate = db.get(Candidate, candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato não encontrado")
    data = payload.model_dump()
    data["profession"] = normalize_profession(payload.profession)
    for key, value in data.items():
        setattr(candidate, key, value)
    audit(db, action="update", entity="candidate", entity_id=str(candidate.id), actor=user.username, details=candidate.name)
    db.commit()
    db.refresh(candidate)
    return candidate


@router.delete("/{candidate_id}", status_code=204)
def delete_candidate(candidate_id: int, user: User = Depends(admin_user), db: Session = Depends(get_db)):
    candidate = db.get(Candidate, candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato não encontrado")
    audit(db, action="delete", entity="candidate", entity_id=str(candidate.id), actor=user.username, details=candidate.name)
    db.delete(candidate)
    db.commit()


@router.get("/{candidate_id}/matches")
def candidate_matches(candidate_id: int, _: User = Depends(current_user), db: Session = Depends(get_db)):
    candidate = db.get(Candidate, candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato não encontrado")
    return [{"id": vacancy.id, "code": vacancy.code, "title": vacancy.title, "profession": vacancy.profession, "city": vacancy.city} for vacancy in match_vacancies(db, candidate)]
