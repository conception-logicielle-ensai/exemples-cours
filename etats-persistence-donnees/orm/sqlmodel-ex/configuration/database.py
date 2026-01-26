from datetime import datetime
from sqlmodel import Field, SQLModel, create_engine, Session
from typing import Generator, Optional

# Important: importer ces modèles
from model.user import User  # noqa: F401

DATABASE_URL = "sqlite:///./utilisateurs.db"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    """Initialise la base de données"""
    print("initialisation de la bdd ...")
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Dépendance pour obtenir une session DB"""
    with Session(engine) as session:
        yield session
