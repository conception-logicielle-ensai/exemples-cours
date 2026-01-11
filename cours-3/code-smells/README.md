# Lancement du programme

## Travail en environnement virtuel

Il est fortement recommandé de prendre l’habitude de travailler dans un environnement virtuel afin d’isoler les dépendances du projet et d’éviter les conflits avec d’autres applications Python.

Depuis la racine du projet, exécutez les commandes suivantes :

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Une fois votre travail terminé, vous pouvez quitter l’environnement virtuel avec la commande suivante :

```bash
deactivate
```

---

## Exécution des programmes

Pour lancer un programme, utilisez la commande suivante :

```bash
python3 nom_du_programme.py
```

où `nom_du_programme.py` correspond au fichier Python à exécuter, par exemple :

* `magic_number.py`