from fastapi import APIRouter
from models.pokemon import Pokemon
from models.pokemon_base import PokemonBase
from services.pokemon_service import PokemonService
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Pokemon"])
pokemon_service = PokemonService()

@router.get("/pokemon/", summary="Récupérer un pokemon", description="Récupérer un pokemon à partir de son nom.")
async def search_pokemon(nom: str):
    """Recherche un Pokémon par nom ou ID."""
    pokemon = pokemon_service.get_pokemon(nom)
    
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon non trouvé")
    
    # Convertir les données en PokemonBase
    return pokemon_service.convert_to_pokemon_base(pokemon)
