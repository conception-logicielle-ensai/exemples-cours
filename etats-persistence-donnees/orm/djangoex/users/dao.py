from typing import Optional, List
from .models import User

class UserDAO:
    """Data Access Object - Gère l'accès aux données en base"""
    
    def create(self, user: User) -> User:
        """Insère un utilisateur en base"""
        user.save()
        return user
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Récupère un utilisateur par son ID"""
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Récupère un utilisateur par son email"""
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Récupère tous les utilisateurs avec pagination"""
        return list(User.objects.all()[skip:skip + limit])
    
    def update(self, user: User) -> User:
        """Met à jour un utilisateur en base"""
        user.save()
        return user
    
    def delete(self, user: User) -> None:
        """Supprime un utilisateur de la base"""
        user.delete()
    
    def exists_by_email(self, email: str) -> bool:
        """Vérifie si un email existe déjà"""
        return User.objects.filter(email=email).exists()
