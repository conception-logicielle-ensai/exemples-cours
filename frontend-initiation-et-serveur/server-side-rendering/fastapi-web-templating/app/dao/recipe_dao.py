# services.py
from typing import List, Optional
from model.recipe import Recipe
# Base de données simulée : une liste de recettes en mémoire
class RecipeDAO:
    def __init__(self):
        self.recipes_db: List[Recipe] = [
        Recipe(
            id=1,
            title="Tarte aux pommes",
            ingredients="Pommes, pâte brisée, sucre, cannelle",
            instructions="Découper les pommes, disposer sur la pâte, saupoudrer de sucre et de cannelle, enfourner 30 minutes.",
            description="Une délicieuse tarte traditionnelle."
        ),
        Recipe(
            id=2,
            title="Quiche lorraine",
            ingredients="Pâte brisée, lardons, crème fraîche, œufs, fromage",
            instructions="Mélanger les œufs et la crème, ajouter les lardons et le fromage, verser sur la pâte et cuire 40 minutes.",
            description="Une quiche savoureuse et facile à préparer."
        ),
    ]

    def get_all_recipes(self) -> List[Recipe]:
        return self.recipes_db 

    def get_recipe_by_id(self,recipe_id: int) -> Optional[Recipe]:
        for recipe in self.recipes_db:
            if recipe.id == recipe_id:
                return recipe
        return None
    def add_recipe(self, recipe:Recipe):
       self.recipes_db.append(recipe)
       return recipe