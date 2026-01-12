# Lancement du programme

## Travail en environnement virtuel

Il est fortement recommandé de prendre l’habitude de travailler dans un environnement virtuel afin d’isoler les dépendances du projet.

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

## Programme chargeant le fichier `.env`

Les fichiers `.env` ne sont généralement pas versionnés, car ils sont exclus par le fichier `.gitignore`.

Pour créer un fichier `.env` de configuration locale, exécutez la commande suivante :

```bash
cat <<EOF > .env
# Configuration par défaut en local
CHEMIN_FICHIER_LOG=
ENVIRONNEMENT=local
EOF
```

Cette commande crée un fichier `.env` contenant deux variables d’environnement :

* `CHEMIN_FICHIER_LOG`
* `ENVIRONNEMENT`

Pour lancer le programme qui charge ce fichier, exécutez la commande suivante depuis le répertoire courant :

```bash
python3 ./load_fichier_env.py
```

---

## Programme chargeant le fichier `.env.local` s’il est présent

Dans cette version du programme, un fichier `.env.local` est chargé en priorité s’il existe, sinon le fichier `.env` est utilisé comme valeur de repli.

Pour lancer le programme, exécutez la commande suivante depuis le répertoire courant :

```bash
python3 ./load_fichier_env.py
```

## Programme chargeant les fichier d'environnement avec `uv`

Dans cette ersionne on charge les variables d'environnement au moment du runtime avec `uv`.
Pour lancer le programme, lancez les commendes 

```bash
uv venv
source .venv/bin/activate
uv run --env-file .env.local python3 load_fichier_dotenv_uv.py
```