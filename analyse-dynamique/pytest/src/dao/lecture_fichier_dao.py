import logging
from pathlib import Path
from typing import Iterable
import requests

logger = logging.getLogger(__name__)


class LectureFichierDAO:
    """
    Classe pour lire un fichier local ou distant (HTTP/HTTPS).
    """

    def _is_file_on_a_remote(self, chemin_fichier_str):
        return chemin_fichier_str.startswith(
            "http://"
        ) or chemin_fichier_str.startswith("https://")

    def _lire_lignes_remote_file(self, url: str):
        try:
            r = requests.get(url, stream=True)
            r.raise_for_status()
            # itération ligne par ligne en lecture
            for raw_line in r.iter_lines(decode_unicode=True):
                yield raw_line
        except Exception as e:
            logger.error(f"Impossible de télécharger '{url}': {e}")
            return  # générateur vide pour pouvoir continuer le process

    def _lire_lignes_local_file(self, base_dir: str, chemin_fichier_str: str):
        chemin_fichier = Path(base_dir) / chemin_fichier_str
        if not chemin_fichier.exists():
            logger.error(
                f"Le fichier '{chemin_fichier_str}' n'existe pas dans le repertoire {base_dir}"
            )
            return  # générateur vide pour pouvoir continuer le process
        try:
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                yield from f
        except Exception as e:
            logger.error(f"Impossible de lire '{chemin_fichier_str}': {e}")
            return  # générateur vide pour pouvoir continuer le process

    def lire_lignes(self, base_dir: str, chemin_fichier_str: str) -> Iterable[str]:
        if self._is_file_on_a_remote(chemin_fichier_str=chemin_fichier_str):
            return self._lire_lignes_remote_file(url=chemin_fichier_str)
        return self._lire_lignes_local_file(
            base_dir=base_dir, chemin_fichier_str=chemin_fichier_str
        )
