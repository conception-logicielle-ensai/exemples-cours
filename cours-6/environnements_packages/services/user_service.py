from typing import Optional

from business_object.user import User
from dao.user_dao import UserDAO
from dto.user_dto import UserDTO


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def peut_se_connecter(self, user: User) -> bool:
        """Vérifie si l'utilisateur peut se connecter (uniquement pour les administrateurs)."""
        return user.is_admin()

    def get_user(self, user_dto: UserDTO):
        user = user_dto.to_user()
        updated_user = self.user_dao.get_user_by_username(user.username)
        return updated_user

    def get_users(self):
        return self.user_dao.get_users()

    def save_user(self, name: str, roles: Optional[tuple[str]]):
        return self.user_dao.save_user(name=name, roles=roles)

    @staticmethod
    def of_context():
        user_dao = UserDAO.of_context()
        return UserService(user_dao=user_dao)
