from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from service.recipe_service import RecipeService 

router = APIRouter()

# Dans la vraie vie, privilégiez un singleton ou il faut que le service ne soit pas stateful (état de la base de données)
recipe_service = RecipeService()
templates = Jinja2Templates(directory="templates")

@router.get("/recipes", response_class=HTMLResponse)
async def recipe_list(request: Request):
    recipes = recipe_service.get_all_recipes()
    return templates.TemplateResponse("recipe_list.html", {"request": request, "recipes": recipes})

@router.get("/recipes/{recipe_id}", response_class=HTMLResponse)
async def recipe_detail(request: Request, recipe_id: int):
    recipe = recipe_service.get_recipe_by_id(recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return templates.TemplateResponse("recipe_detail.html", {"request": request, "recipe": recipe})

@router.get("/search", response_class=HTMLResponse)
async def search_recipe(request: Request, recipe_id: int = None):
    if recipe_id is None:
        # On renvoie l'index avec un message d'erreur si aucun ID n'est fourni
        return templates.TemplateResponse("index.html", {"request": request, "error": "Veuillez saisir un ID."})
    recipe = recipe_service.get_recipe_by_id(recipe_id)
    if not recipe:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Recette non trouvée."})
    return templates.TemplateResponse("recipe_detail.html", {"request": request, "recipe": recipe})

@router.get("/recipes/new", response_class=HTMLResponse)
async def new_recipe(request: Request):
    # Optionnel : si vous souhaitez une page dédiée pour l'ajout
    return templates.TemplateResponse("new_recipe.html", {"request": request})

@router.post("/recipes/new", response_class=HTMLResponse)
async def create_recipe(
    request: Request,
    title: str = Form(...),
    ingredients: str = Form(...),
    instructions: str = Form(...),
    description: str = Form(None)
):
    recipe = recipe_service.add_recipe(title, ingredients, instructions, description)
    return templates.TemplateResponse("recipe_detail.html", {"request": request, "recipe": recipe})