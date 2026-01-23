from fastapi import APIRouter
from models.item import Item
from services.item_service import ItemService

router = APIRouter(tags=["Items"])
item_service = ItemService()

@router.post("/items/", summary="Créer un article", description="Crée un nouvel article avec les détails fournis.")
async def create_item(item: Item) -> Item:
    """
    Crée un nouvel article avec les informations fournies dans le corps de la requête.
    
    - **item**: Détails de l'article à créer.
    
    Renvoie l'article créé.
    """
    return item_service.create_item(item)

@router.get("/items/", summary="Lire les articles", description="Récupère une liste d'articles prédéfinis.")
async def read_items() -> list[Item]:
    """
    Récupère une liste d'articles prédéfinis.

    Renvoie une liste d'articles avec des noms et des prix.
    """
    return item_service.get_items()
