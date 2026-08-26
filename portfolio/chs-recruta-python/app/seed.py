from __future__ import annotations

from sqlalchemy import select

from .database import Base, SessionLocal, engine
from .models import Role, User
from .security import hash_password


def main() -> None:
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        if db.scalar(select(User).where(User.username == "demo")):
            print("Usuário demo já existe.")
            return
        db.add(
            User(
                username="demo",
                display_name="Administradora Demo",
                email="demo@chs.local",
                password_hash=hash_password("demo12345"),
                role=Role.admin,
            )
        )
        db.commit()
    print("Criado usuário demo / demo12345. Use somente em ambiente de demonstração.")


if __name__ == "__main__":
    main()
