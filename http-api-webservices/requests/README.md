### Installation des dépendances
```bash
pip install -r cours-4/requests/requirements.txt
```

### Démarrage de l'application en local
```bash
python cours-4/requests/main.py
```

### Accès à Swagger
L'interface Swagger est accessible à l'URL suivante : `http://127.0.0.1:8000/docs`

## Explication

Dans la classe `PokemonService` du module `pokemon_service`, nous avons implémenté un système de désérialisation pour récupérer les données des Pokémon à partir de l'API disponible à l'URL `https://pokeapi-proxy.freecodecamp.rocks/api/pokemon`. En utilisant le module `requests`, nous effectuons une requête de type GET pour obtenir les informations des Pokémon. Cette désérialisation nous permet de transformer les données brutes renvoyées par l'API en objets utilisables dans notre application.