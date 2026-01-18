from functools import reduce
import logging
from pathlib import Path
from typing import Iterable, Optional
from src.model.compteur import Compteur
from src.dao.lecture_fichier_dao import LectureFichierDAO
logger = logging.getLogger(__name__)


class CompteurService:

    def __init__(self, lecture_fichier_dao:LectureFichierDAO = LectureFichierDAO()):
        self.__lecture_fichier_dao = lecture_fichier_dao
    def recuperer_informations_caracteres_fichier(
        self, base_dir:str, chemin_fichier_str: str
    ) -> Optional[dict]:
        """
        Lit un fichier et compte les occurrences de chaque lettre.

        Args:
            chemin_fichier: Le chemin vers le fichier à analyser

        Returns:
            Dictionnaire avec le compte de chaque lettre, ou None en cas d'erreur
        """

        lignes = self.__lecture_fichier_dao.lire_lignes(base_dir=base_dir, chemin_fichier_str=chemin_fichier_str)
        compteur = Compteur(lignes)
        return compteur.characters_data
