from sqlmodel import Session, select
from typing import Optional
from model.user import User

class UserDAO:
    """Data Access Object - Gère l'accès aux données en base"""
    
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, user: User) -> User:
        """Insère un utilisateur en base"""
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Récupère un utilisateur par son ID"""
        return self.session.get(User, user_id)
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Récupère un utilisateur par son email"""
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()
    
    def get_all(self, skip: int = 0, limit: int = 100) -> list[User]:
        """Récupère tous les utilisateurs avec pagination"""
        statement = select(User).offset(skip).limit(limit)
        return list(self.session.exec(statement).all())
    
    def update(self, user: User) -> User:
        """Met à jour un utilisateur en base"""
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def delete(self, user: User) -> None:
        """Supprime un utilisateur de la base"""
        self.session.delete(user)
        self.session.commit()
    
    def exists_by_email(self, email: str) -> bool:
        """Vérifie si un email existe déjà"""
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first() is not None
