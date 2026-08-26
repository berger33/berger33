from __future__ import annotations

import csv
import io

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import AuditLog, Candidate, FinancialReference, User
from ..schemas import DashboardRead, FinancialCreate, FinancialRead
from ..security import current_user
from ..services import audit, dashboard

router = APIRouter(prefix="/api", tags=["operations"])


@router.get("/dashboard", response_model=DashboardRead)
def get_dashboard(_: User = Depends(current_user), db: Session = Depends(get_db)):
    return dashboard(db)


@router.get("/audit")
def list_audit(_: User = Depends(current_user), db: Session = Depends(get_db)):
    rows = db.scalars(select(AuditLog).order_by(AuditLog.created_at.desc()).limit(200)).all()
    return [{"id": row.id, "action": row.action, "entity": row.entity, "entity_id": row.entity_id, "actor": row.actor, "details": row.details, "created_at": row.created_at} for row in rows]


@router.get("/financial", response_model=list[FinancialRead])
def list_financial(_: User = Depends(current_user), db: Session = Depends(get_db)):
    return db.scalars(select(FinancialReference).order_by(FinancialReference.service)).all()


@router.post("/financial", response_model=FinancialRead, status_code=201)
def create_financial(payload: FinancialCreate, user: User = Depends(current_user), db: Session = Depends(get_db)):
    item = FinancialReference(**payload.model_dump())
    db.add(item)
    db.flush()
    audit(db, action="create", entity="financial", entity_id=str(item.id), actor=user.username, details=item.service)
    db.commit()
    db.refresh(item)
    return item


@router.get("/reports/candidates.csv")
def export_candidates(_: User = Depends(current_user), db: Session = Depends(get_db)):
    output = io.StringIO()
    writer = csv.writer(output, delimiter=";")
    writer.writerow(["id", "nome", "profissao", "cidade", "telefone", "email", "status", "vaga_id", "recrutador"])
    for candidate in db.scalars(select(Candidate).order_by(Candidate.name)).all():
        writer.writerow([candidate.id, candidate.name, candidate.profession, candidate.city, candidate.phone, candidate.email, candidate.status.value, candidate.vacancy_id or "", candidate.recruiter])
    data = "\ufeff" + output.getvalue()
    return StreamingResponse(iter([data]), media_type="text/csv; charset=utf-8", headers={"Content-Disposition": "attachment; filename=candidatos.csv"})
