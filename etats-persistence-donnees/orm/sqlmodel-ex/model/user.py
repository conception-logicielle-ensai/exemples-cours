from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    """Modèle de base de données - représentation interne"""
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    nom: str
    prenom: str
    age: int
    actif: bool = Field(default=True)
    date_creation: datetime = Field(default_factory=datetime.now)


