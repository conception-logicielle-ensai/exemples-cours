# pip-compile

Projet avec pip compile

Installer avec :
```sh
python -m venv .venv
source /.venv/bin/activate
pip install pip-tools
```
1. Création d'un requirements.in

2. Puis

```sh
pip-compile
```

> Cette commande génère le fichier requirements.txt FIXE

3. Puis pour installer le projet dans le venv
```sh
pip-sync
```

Pour mettre a jour des dépendances il faudra ensuite faire : 
```
pip-compile --upgrade
```

## Getting started

Pour démarrer le projet

- Créer un venv : python -m venv .venv
- Activer le venv: source .venv/bin/activate
- Installer pip-tools : `pip install pip-tools`
- Installer les dépendances : `pip-sync`

Puis lancer l'application:
`python app.py`