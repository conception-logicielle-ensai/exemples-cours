from dotenv import load_dotenv

# Charge toutes les variables d'environnement depuis le fichier .env
load_dotenv()

import os

chemin_fichier_log = os.getenv("CHEMIN_FICHIER_LOG")
environnement = os.getenv("ENVIRONNEMENT")

print(chemin_fichier_log)
print(environnement)