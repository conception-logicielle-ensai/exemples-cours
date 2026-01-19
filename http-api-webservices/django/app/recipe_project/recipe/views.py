from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .service import *

def recipe_list(request):
    recipes = get_all_recipes()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_recipe_raises_404(recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
def search_recipe(request):
    query_parameter_recipe_id = request.GET.get('recipe_id')  # Récupération du paramètre de l'URL
    if query_parameter_recipe_id is None:
        return render(request, 'recipes/index.html', {'error': f"Le paramètre id est non renseigné"})
    recipe = get_recipe_nullable(query_parameter_recipe_id)
    if recipe is None:
        return render(request, 'recipes/index.html', {'error': f"La recette avec l'id {query_parameter_recipe_id} n'existe pas"})
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@csrf_exempt
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            persist_form(form)
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

def home(request):
    return render(request, 'recipes/index.html')