# models.py
from pydantic import BaseModel
from typing import Optional

class Recipe(BaseModel):
    id: int
    title: str
    ingredients: str
    instructions: str
    description: Optional[str] = None
    ## Factory ça doit vous rappeler quelque chose.
    @classmethod
    def create_recipe(cls, id: int, title: str, ingredients: str, instructions: str, description: Optional[str] = None):
        """
        Méthode de classe servant de constructeur alternatif.
        Elle renseigne tous les champs requis et optionnels.
        """
        return cls(
            id=id,
            title=title,
            ingredients=ingredients,
            instructions=instructions,
            description=description
        )