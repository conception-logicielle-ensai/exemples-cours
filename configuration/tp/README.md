# TP – Configuration du code en fonction de l'environnement

## Lancement de l’application

### Prérequis

Avant de lancer l’application, assurez-vous de disposer des éléments suivants :

* **Python 3.11 ou supérieur**
* **uv** installé et accessible depuis le terminal

---

### Création de l’environnement et installation des dépendances

Depuis la racine du projet, exécutez les commandes suivantes :

```bash
uv venv
```

Cet commande permet de créer l’environnement virtuel du projet.

---

### Lancement du script

Une fois l’environnement configuré, lancez le script avec la commande suivante :

```bash
uv run --env-file .env.local python3 ./main.py
```

Vérifiez que les variables d'envrionnes suivantes sont présentes :
- BDD_URL
- BDD_MDP
- APP_VERSION