# Appli avec architecture coherente 

## Getting started

1. installation des dépendances: `pip install -r requirements.txt`

2. **Pour la suite on se situera dans le dossier app** (voir le Readme dans le dossier app)


## Archi

### Code global post génération

```
app/ - le répertoire racine de notre repository
    requirements.txt - une liste des packages requis pour lancer l'appli
    recipe_project/ - le répertoire contenant notre projet Django, l'application, la base de données et l'utilitaire de ligne de commande
        manage.py - le script utilitaire de ligne de commande de Django
        db.sqlite3 - le fichier de la base de données de Django
        recipe_project/ - le répertoire du projet, généré par « django-admin startproject projet_exemplesimple » : la « tour de contrôle » de notre projet
            settings.py - la configuration de l'ensemble du projet
            ...et d'autres fichiers relatifs au projet. 
        recipe/ - le répertoire de l’application généré par « python manage.py startapp exemplesimple »
            ...les fichiers spécifiques aux applications que nous explorerons tout au long du cours
```


## Comment créer la meme app

1. `pip install django`
2. `django-admin startproject recipe_project`
3. `cd recipe_project` (on se met dans le projet pour mettre en place l'appli dans le projet django)
4. `python manage.py startapp recipe`

5. Configurations spécifiques : Jinja2

=> On met en place la configuration pour utiliser le templating jinja2 plutôt que django, vous pouvez ne pas le faire.
Ajout de `jinja2` aux requirements et 

ajouter un environnement de resolution de template jinja2:
Dans `recipe_project/settings.py`
```python
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',  # Utilisation de Jinja2
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'recipe.jinja2.environment',  # Définir un environnement Jinja2 personnalisé
        },
    },
```

6. Ajout de l'appli "recipe" a la liste des apps installées : 

- Dans `settings.py`, dans la variable globale INSTALLED_APPS, ajout de  "recipe"

7. Mise en place du modèle des recettes et migrations

```
python manage.py makemigrations # mise a jour du modele de bdd
python manage.py migrate
```

8. Mise en place des vues

- Routing: path('recipes/', include('recipe.urls')) dans `manage.py` de recipe_project
- Urls et vues pour l'aspect "métier"

Templates copiés dans templates/

9. Ajout de la configuration static pour le css et favicon

Dans la configuration `settings.py`:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
