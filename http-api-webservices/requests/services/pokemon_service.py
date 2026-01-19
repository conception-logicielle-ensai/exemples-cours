import requests
from models.pokemon import Pokemon
from models.pokemon_base import PokemonBase

class PokemonService:
    BASE_URL = "https://pokeapi-proxy.freecodecamp.rocks/api/pokemon"

    @staticmethod
    def fetch_pokemon_list():
        """Récupère la liste complète des Pokémon avec leur ID et nom."""
        response = requests.get(PokemonService.BASE_URL)
        response.raise_for_status()
        return response.json()["results"]

    @staticmethod
    def get_pokemon(name):
        """Récupère un Pokémon par son ID ou son nom."""
        try:
            pokemons = PokemonService.fetch_pokemon_list()
            pokemon_data = next((p for p in pokemons if p["name"] == name.lower()), None) # récupère le premier élément correspondant, ou None si aucun Pokémon ne correspond.

            if not pokemon_data:
                return None

            # Récupérer les détails complets du Pokémon
            response = requests.get(f"{PokemonService.BASE_URL}/{pokemon_data['id']}")
            response.raise_for_status()
            data = response.json()

            # Extraire les informations utiles
            stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
            types = [t["type"]["name"] for t in data["types"]]
            sprite = data["sprites"]["front_default"]

            return Pokemon(
                id_=data["id"],
                name=data["name"],
                weight=data["weight"],
                height=data["height"],
                types=types,
                stats=stats,
                sprite=sprite,
            )
        except requests.RequestException as e:
            print(f"Erreur de récupération des données : {e}")
            return None
    
    @staticmethod
    def convert_to_pokemon_base(pokemon: Pokemon) -> PokemonBase:
        """Convertit un objet Pokemon en un objet PokemonBase."""
        return PokemonBase(
            id=pokemon.id,
            name=pokemon.name,
            weight=pokemon.weight,
            height=pokemon.height
        )

