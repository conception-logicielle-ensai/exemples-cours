# Déploiement d'une API FastAPI avec PostgreSQL et Docker

## Prérequis
Avant de commencer, assurez-vous d'avoir installé :
- [Docker](https://www.docker.com/)

## 1. Démarrer un conteneur PostgreSQL
Nous allons utiliser Docker pour exécuter une instance de PostgreSQL.

Exécutez la commande suivante pour lancer un conteneur PostgreSQL :

```sh
docker run --name postgres_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -p 5432:5432 -d postgres
```

Cette commande :
- Crée un conteneur nommé `postgres_db`
- Définit les variables d'environnement pour l'utilisateur, le mot de passe et la base de données
- Expose PostgreSQL sur le port `5432`
- Exécute PostgreSQL en arrière-plan

## 2. Construire et exécuter le conteneur FastAPI
Une fois la base de données en cours d'exécution, nous pouvons construire et exécuter l'API.

### Construire l'image Docker
Exécutez la commande suivante dans le répertoire du projet :

```sh
docker build -t fastapi_app .
```

### Lancer le conteneur FastAPI

```sh
docker run --name fastapi_container --env DB_HOST=postgres_db --env DB_USER=postgres --env DB_PASSWORD=postgres --env DB_NAME=postgres --env DB_PORT=5432 -p 8000:8000 --link postgres_db -d fastapi_app
```

Cette commande :
- Crée un conteneur nommé `fastapi_container`
- Configure la connexion à PostgreSQL via les variables d'environnement
- Expose FastAPI sur le port `8000`
- Lie le conteneur à `postgres_db` pour lui permettre d’accéder à la base de données
- Exécute FastAPI en arrière-plan

## 3. Vérifier si l'API fonctionne

Une fois l'application en cours d'exécution, ouvrez un navigateur ou utilisez `curl` pour tester l'API :

```sh
curl http://localhost:8000/docs
```

L'interface Swagger devrait être disponible à l'adresse : [http://localhost:8000/docs](http://localhost:8000/docs)

## 4. Arrêter et supprimer les conteneurs
Pour arrêter les conteneurs :

```sh
docker stop fastapi_container postgres_db
```

Pour les supprimer :

```sh
docker rm fastapi_container postgres_db
```
