"""
Ici on cumule deux notions : le mocking et l'injection de dépendances
Les classes de service ne portent pas forcément le coeur de métier, mais cela peut être le cas.
Par contre la dépendance a la DAO
Peut être assez lourde pour la reproductibilité.
Donc on va plutôt Mocker les DAO pour tester le comportement uniquement du service,
Comme un orchestrateur de processus
"""

import pytest
from src.dao.lecture_fichier_dao import LectureFichierDAO
from src.service.compteur_service import CompteurService


@pytest.fixture
def dao(mocker) -> LectureFichierDAO:
    """Fixture simple : retourne une instance de LectureFichierDAO"""
    dao = LectureFichierDAO()

    # Patch la méthode lire_lignes pour qu'elle retourne toujours ["abcd","bcde"]
    mocker.patch.object(
        dao,
        "lire_lignes",
        return_value=iter(["abcd", "bcde"]),  # retourne un itérateur, comme le vrai
    )
    return dao


@pytest.fixture
def service(dao) -> CompteurService:
    """
    On injecte le mock direct, c'est trop bien non?
    """
    return CompteurService(lecture_fichier_dao=dao)


class TestLireFichier:
    def test_lire_lignes_remote_file_mocking_requests(self, service: CompteurService):
        """
        Ici on va tester la fonction _lire_lignes_remote_file
        Cette fonction est appellée dans lire_lignes_remote_file
        Il faut garder en tête qu'on ne pourra pas tout tester et donc focus les fonctions que l'on
        met a disposition pour les autres modules, les fonctions publiques
        """
        informations = service.recuperer_informations_caracteres_fichier(
            "peu-importe-cest-mocke", "peu-importe-cest-mocke"
        )

        print(informations)
        # Assert
        assert informations == {
            "comptage_par_lettre": {"a": 1, "b": 2, "c": 2, "d": 2, "e": 1},
            "nb_caracteres": 8,
            "nb_lignes": 2,
        }
