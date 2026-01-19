## Démarrer l'application

Pour exécuter l'application en local, suivez ces étapes :

### Installation des dépendances
```bash
pip install -r cours-4/webservice/requirements.txt
```

### Démarrage de l'application en local
```bash
cd cours-4/fastapi
uvicorn main:app --reload
```

### Accès à Swagger
L'interface Swagger est accessible à l'URL suivante : `http://127.0.0.1:8000/docs`