from __future__ import annotations

import os
from pathlib import Path

os.environ["DATABASE_URL"] = "sqlite:///./test_chs_recruta.db"

from fastapi.testclient import TestClient
from sqlalchemy import select

from app.database import Base, SessionLocal, engine
from app.main import app
from app.models import Role, User
from app.security import hash_password

client = TestClient(app)
TEST_DB = Path("test_chs_recruta.db")


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        db.add(User(username="demo", display_name="Admin Demo", email="demo@example.com", password_hash=hash_password("demo12345"), role=Role.admin))
        db.commit()


def auth_headers() -> dict[str, str]:
    response = client.post("/api/auth/login", json={"username": "demo", "password": "demo12345"})
    assert response.status_code == 200
    return {"Authorization": f"Bearer {response.json()['access_token']}"}


def test_health_and_auth_boundary():
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/api/dashboard").status_code == 401
    headers = auth_headers()
    me = client.get("/api/auth/me", headers=headers)
    assert me.status_code == 200
    assert me.json()["role"] == "admin"


def test_candidate_normalization_duplicate_and_dashboard():
    headers = auth_headers()
    payload = {"name": "Ana Silva", "profession": "Enfermeira", "city": "São Paulo", "phone": "11999990000", "email": "ana@example.com", "recruiter": "demo"}
    created = client.post("/api/candidates", json=payload, headers=headers)
    assert created.status_code == 201
    assert created.json()["profession"] == "Enfermeiro"
    duplicate = client.post("/api/candidates", json=payload, headers=headers)
    assert duplicate.status_code == 409
    dashboard = client.get("/api/dashboard", headers=headers).json()
    assert dashboard["candidates"] == 1
    assert dashboard["new_candidates"] == 1


def test_vacancy_matching():
    headers = auth_headers()
    vacancy = client.post("/api/vacancies", headers=headers, json={"code": "ENF-001", "title": "Enfermagem", "profession": "Enfermeiro", "city": "São Paulo", "positions": 2, "owner": "demo"})
    assert vacancy.status_code == 201
    candidate = client.post("/api/candidates", headers=headers, json={"name": "Maria", "profession": "Enfermeira", "city": "São Paulo", "phone": "11888880000"})
    assert candidate.status_code == 201
    matches = client.get(f"/api/candidates/{candidate.json()['id']}/matches", headers=headers)
    assert matches.status_code == 200
    assert matches.json()[0]["code"] == "ENF-001"


def test_csv_and_admin_user_management():
    headers = auth_headers()
    client.post("/api/candidates", headers=headers, json={"name": "Carlos", "profession": "Psicólogo", "phone": "11777770000"})
    report = client.get("/api/reports/candidates.csv", headers=headers)
    assert report.status_code == 200
    assert "Carlos" in report.text
    new_user = client.post("/api/users", headers=headers, json={"username": "recruiter", "display_name": "Recruiter", "email": "recruiter@example.com", "password": "senha12345", "role": "recruiter"})
    assert new_user.status_code == 201
    users = client.get("/api/users", headers=headers)
    assert users.status_code == 200
    assert {user["username"] for user in users.json()} == {"demo", "recruiter"}
