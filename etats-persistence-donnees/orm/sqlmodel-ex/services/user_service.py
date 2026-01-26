from typing import Optional
from model.user import User
from dto.dtos import UserCreate, UserUpdate
from dao.user_dao import UserDAO

class UserService:
    """Service gérant la logique métier des utilisateurs"""
    
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao
    
    def creer_utilisateur(self, user_data: UserCreate) -> User:
        """Crée un nouvel utilisateur avec validation métier"""
        # Validation : vérifier que l'email n'existe pas déjà
        if self.user_dao.exists_by_email(user_data.email):
            raise ValueError(f"L'email {user_data.email} existe déjà")
        
        # Validation : âge minimum
        if user_data.est_mineur():
            raise ValueError("L'utilisateur doit avoir au moins 18 ans")
        
        # Créer l'entité User à partir du DTO
        user = User(**user_data.model_dump())
        
        # Déléguer la persistance au DAO
        return self.user_dao.create(user)
    
    def obtenir_utilisateur(self, user_id: int) -> Optional[User]:
        """Récupère un utilisateur par ID"""
        return self.user_dao.get_by_id(user_id)
    
    def obtenir_tous_utilisateurs(self) -> list[User]:
        """Récupère tous les utilisateurs"""
        return self.user_dao.get_all()
    
    def mettre_a_jour_utilisateur(
        self, user_id: int, user_data: UserUpdate
    ) -> Optional[User]:
        """Met à jour un utilisateur avec validation métier"""
        # Récupérer l'utilisateur existant
        user = self.user_dao.get_by_id(user_id)
        if not user:
            return None
        
        # Valider les données mises à jour
        update_dict = user_data.model_dump(exclude_unset=True)
        
        if "email" in update_dict and update_dict["email"] != user.email:
            # Vérifier que le nouvel email n'est pas déjà pris
            if self.user_dao.exists_by_email(update_dict["email"]):
                raise ValueError(f"L'email {update_dict['email']} existe déjà")
        
        if "age" in update_dict and update_dict["age"] < 18:
            raise ValueError("L'utilisateur doit avoir au moins 18 ans")
        
        # Appliquer les modifications
        for key, value in update_dict.items():
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

