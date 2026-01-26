from typing import Optional, Dict, Any
from .models import User
from .dao import UserDAO

class UserService:
    """Service gérant la logique métier des utilisateurs"""
    
    def __init__(self):
        self.user_dao = UserDAO()
    
    def creer_utilisateur(self, user_data: Dict[str, Any]) -> User:
        """Crée un nouvel utilisateur avec validation métier"""
        # Validation : vérifier que l'email n'existe pas déjà
        if self.user_dao.exists_by_email(user_data['email']):
            raise ValueError(f"L'email {user_data['email']} existe déjà")
        
        # Validation : âge minimum
        if user_data['age'] < 18:
            raise ValueError("L'utilisateur doit avoir au moins 18 ans")
        
        # Créer l'entité User
        user = User(**user_data)
        
        # Déléguer la persistance au DAO
        return self.user_dao.create(user)
    
    def obtenir_utilisateur(self, user_id: int) -> Optional[User]:
        """Récupère un utilisateur par ID"""
        return self.user_dao.get_by_id(user_id)
    
    def obtenir_tous_utilisateurs(self) -> list[User]:
        """Récupère tous les utilisateurs"""
        return self.user_dao.get_all()
    
    def mettre_a_jour_utilisateur(
        self, user_id: int, user_data: Dict[str, Any]
    ) -> Optional[User]:
        """Met à jour un utilisateur avec validation métier"""
        # Récupérer l'utilisateur existant
        user = self.user_dao.get_by_id(user_id)
        if not user:
            return None
        
        # Valider les données mises à jour
        if "email" in user_data and user_data["email"] != user.email:
            # Vérifier que le nouvel email n'est pas déjà pris
            if self.user_dao.exists_by_email(user_data["email"]):
                raise ValueError(f"L'email {user_data['email']} existe déjà")
        
        if "age" in user_data and user_data["age"] < 18:
            raise ValueError("L'utilisateur doit avoir au moins 18 ans")
        
        # Appliquer les modifications
        for key, value in user_data.items():
            setattr(user, key, value)
        
        # Persister via le DAO
        return self.user_dao.update(user)
    
    def supprimer_utilisateur(self, user_id: int) -> bool:
        """Supprime un utilisateur"""
        user = self.user_dao.get_by_id(user_id)
        if not user:
            return False
        
        self.user_dao.delete(user)
        return True
