# Hello Ensai

## Démarrer le projet

```sh
uv sync
uv run python -m helloensai
```

- `uv sync` permet de récupérer la version de python qui matche le pyproject et installer les dépendances, uv va stocker tout ça dans un `.venv`.
- `uv run` permet d'utiliser l'environnement virtuel ainsi crée pour lancer le programme.

## Publication
Pour publier avec UV, il faut bien configurer son projet et notamment le fichier pyproject.toml.

- Par défaut uv publie le fichier qui est dans `src`

Vous pouvez y contrevenir en configurant le build tool:
```
[tool.hatch.build.targets.wheel]
packages = ["helloensai"]

[tool.hatch.build.targets.sdist]
include = ["helloensai"]
```

Ensuite il s'agit simplement de construire le `.whl` : 
- `poetry build`
- `poetry publish --token XXXXXXXX`

Le token est à récupérer sur l'instance de PyPi.
