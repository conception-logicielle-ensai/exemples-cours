from datetime import datetime
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlmodel import Session
from configuration.database import get_session
from dto.dtos import UserCreate, UserResponse, UserUpdate
from services.user_service import UserService
from dao.user_dao import UserDAO

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=201)
def creer_utilisateur(user: UserCreate, session: Session = Depends(get_session)):
    """Crée un nouvel utilisateur"""
    try:
        user_service = UserService(user_dao=UserDAO(session))
        user_db = user_service.creer_utilisateur(user)
        return user_db
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserResponse)
def obtenir_utilisateur(user_id: int, session: Session = Depends(get_session)):
    """Récupère un utilisateur par ID"""
    user_service = UserService(user_dao=UserDAO(session))

    user = user_service.obtenir_utilisateur(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user

@router.get("/", response_model=list[UserResponse])
def lister_utilisateurs(session: Session = Depends(get_session)):
    """Liste tous les utilisateurs"""
    user_service = UserService(user_dao=UserDAO(session))
    return user_service.obtenir_tous_utilisateurs()

@router.put("/{user_id}", response_model=UserResponse)
def modifier_utilisateur(
    user_id: int, user: UserUpdate, session: Session = Depends(get_session)
):
    """Met à jour un utilisateur"""
    user_service = UserService(user_dao=UserDAO(session))

    user_db = user_service.mettre_a_jour_utilisateur(user_id, user)
    if not user_db:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user_db

@router.delete("/{user_id}", status_code=204)
def supprimer_utilisateur(user_id: int, session: Session = Depends(get_session)):
    """Supprime un utilisateur"""
    user_service = UserService(user_dao=UserDAO(session))
    
    success = user_service.supprimer_utilisateur(session, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
