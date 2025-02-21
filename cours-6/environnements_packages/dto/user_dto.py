from pydantic import BaseModel, Field

from business_object.user import User


class UserDTO(BaseModel):
    username: str = Field(examples=["adm", "pasadm"])

    def to_user(self):
        """Convert DTO to a plain User object."""
        return User(id=None, username=self.username, roles=None)
