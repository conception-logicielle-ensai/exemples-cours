
from django.shortcuts import get_object_or_404
from .models import Recipe
def get_all_recipes():
    return Recipe.objects.all()
def get_recipe_raises_404(recipe_id):
    return get_object_or_404(Recipe, id=recipe_id)
def get_recipe_nullable(recipe_id):
    try:
        return Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist as e:
        return None
def persist_form(form):
    form.save()