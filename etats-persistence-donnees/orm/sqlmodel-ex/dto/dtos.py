from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserResponse(BaseModel):
    """Schéma de réponse - Output API"""
    id: int
    email: str
    nom: str
    prenom: str
    age: int
    actif: bool
    date_creation: datetime
# Modeles intermédiaires "DTO"
class UserCreate(BaseModel):
    """Schéma pour créer un utilisateur - Input API"""
    email: str
    nom: str
    prenom: str
    age: int
    def est_mineur(self):
        return self.age <18
class UserUpdate(BaseModel):
    """Schéma pour mettre à jour un utilisateur - Input API"""
    email: Optional[str] = None
    nom: Optional[str] = None
    prenom: Optional[str] = None
    age: Optional[int] = None
    actif: Optional[bool] = None
    
