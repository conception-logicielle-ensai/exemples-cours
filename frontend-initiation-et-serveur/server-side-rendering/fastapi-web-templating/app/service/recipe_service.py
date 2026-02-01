from dao.recipe_dao import RecipeDAO
from model.recipe import Recipe
from typing import List, Optional
class RecipeService:
    def __init__(self):
        self.recette_dao = RecipeDAO()

    def get_all_recipes(self) -> List[Recipe]:
        return self.recette_dao.get_all_recipes()

    def get_recipe_by_id(self,recipe_id: int) -> Optional[Recipe]:
        for recipe in self.recette_dao.get_all_recipes():
            if recipe.id == recipe_id:
                return recipe
        return None
    
    def __get_last_index_recipe(self):
        return list(map(lambda recipe: recipe.id, self.get_all_recipes()))[-1]
    def add_recipe(self,title:str, ingredients:str, instructions:str, description:str):
        last_index_plus_un = self.__get_last_index_recipe() + 1
        recipe = Recipe.create_recipe(last_index_plus_un,title=title, ingredients=ingredients, instructions=instructions, description= description)
        return self.recette_dao.add_recipe(recipe)