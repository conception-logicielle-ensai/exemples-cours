# Client HTTP avec gestion de session et API de test

## Installation du projet avec uv

### Pré-requis

* `python` ≥ 3.11
* `uv` installé

### Installation

Depuis la racine du projet :

```bash
uv sync
```

## L’API de test

Une petite API FastAPI est fournie dans le dossier `api` afin de simuler :

* un backend sécurisé par token,
* un endpoint de rafraîchissement,
* une ressource protégée.


### Lancer l’API

Dans un terminal :

```bash
uv run uvicorn api.main:app --reload
```

L’API démarre sur :

```
http://127.0.0.1:8000
```

### Fonctionnement

L’API expose deux endpoints :

**`GET /api/books`**
* Renvoie une liste de livres.
* Vérifie le header `Authorization`.
* Si le token est invalide → retourne **401 Unauthorized**.

**`POST /auth/refresh`**
* Reçoit un `refresh_token`.
* S’il est valide → retourne un nouvel `access_token`.

Cette API est volontairement simplifiée :
elle ne gère ni base de données, ni JWT réels, ni sécurité avancée.

Son objectif est **strictement pédagogique**.

## Client de test

Dans un second terminal, avec l’API toujours active :

```bash
uv run python test_client.py
```

**Ce que fait ce script**

Le fichier `test_client.py` ne contient qu’un appel métier simple : il demande la liste des livres à l’API.

Il utilise pour cela un gestionnaire de session HTTP (HttpSession) chargé de :
- envoyer les headers d’authentification,
- détecter les erreurs 401,
- rafraîchir automatiquement le token,
- rejouer la requête initiale.

Le script de test ne gère aucune logique d’authentification directement.


# Conclusion — Observation des logs côté API

Pendant l’exécution, observez les logs du serveur FastAPI.

Vous devriez voir apparaître une séquence similaire :

```
INFO:     127.0.0.1:64562 - "GET /api/books HTTP/1.1" 401 Unauthorized
INFO:     127.0.0.1:64562 - "POST /auth/refresh HTTP/1.1" 200 OK
INFO:     127.0.0.1:64562 - "GET /api/books HTTP/1.1" 200 OK
```

Ces logs montrent clairement que :

* une première requête a été refusée à cause d’un token invalide,
* le client a automatiquement déclenché le mécanisme de rafraîchissement,
* la requête initiale a ensuite été rejouée avec succès.

Le script de test **n’a pas connaissance** de cette mécanique interne :
elle est entièrement prise en charge par le gestionnaire de session HTTP.

C’est précisément l’objectif de cette abstraction : **rendre transparente la gestion des jetons pour le reste de l’application cliente.**
