## Démarrer l'application

Pour exécuter l'application en local, suivez ces étapes :

### Pré-requis

* `python` ≥ 3.11
* `uv` installé

### Installation des dépendances

```bash
uv sync
```

### Démarrage de l'application en local

```bash
uv run uvicorn main:app --reload
```

### Accès à Swagger
L'interface Swagger est accessible à l'URL suivante : `http://127.0.0.1:8000/docs`