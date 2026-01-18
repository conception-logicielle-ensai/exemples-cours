import os
from src.view.compteur_view import CompteurView
import logging

logging.basicConfig(
    filename="app.log",  # nom du fichier de log
    filemode="a",  # "w" pour écraser à chaque lancement, "a" pour append
    level=logging.INFO,  # niveau de log minimal
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

compteur_view = CompteurView(os.getenv("BASE_DIR", "./samples"))

comptages_exemples = compteur_view.compter_metadonnees_caracteres_fichier(
    "fichier_exemple.txt"
)
comptages_exemples_page_web = compteur_view.compter_metadonnees_caracteres_fichier(
    "https://google.com"
)
comptages_exemples_page_web = compteur_view.compter_metadonnees_caracteres_fichier(
    "https://g22222oogle.com"
)
