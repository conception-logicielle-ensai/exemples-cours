"""
Pour les DAO on souhaite tester le comportement mais on a dépendances externes
2 solutions :
- Soit mettre en place tout un environnement fonctionnel (via des fixtures)
- Ou **mocker**, c'est a dire gérer les appels aux modules externes et leurs retours
"""

import pytest
from src.dao.lecture_fichier_dao import LectureFichierDAO


@pytest.fixture
def dao() -> LectureFichierDAO:
    """Fixture simple : retourne une instance de LectureFichierDAO"""
    return LectureFichierDAO()


# Ensuite ils s'appellent via les arguments des fonctions de test
class TestIsFileOnARemote:
    # Les fixtures peuvent simplement permettre d'éviter de réecrire des bouts de code
    # On peut également chainer les check si ça regroupe la même logique
    def test_https_url_is_well_detected(self, dao: LectureFichierDAO):
        assert dao.is_file_on_a_remote("https://google.com")  # == True
        assert dao.is_file_on_a_remote("local.txt") == False


# Les fixtures permettent aussi de générer des fichiers temporaires ou des ressources temporaires nécessaires pendant les tests
PATH_FICHIER_DE_TEST = "test.txt"
CONTENU_FICHIER_DE_TEST = "abcsd\nasdbc\nazeazez\n"


@pytest.fixture
def fichier_temporaire(tmp_path):
    # pour info tmp_path est injecté comme fixture par défaut
    """
    Fixture qui crée un fichier temporaire pour le test,
    puis le supprime automatiquement après le test
    """
    # Créer le fichier temporaire
    fichier = tmp_path / PATH_FICHIER_DE_TEST
    fichier.write_text(CONTENU_FICHIER_DE_TEST, encoding="utf-8")

    # Fournir le fichier au test
    yield fichier


EXPECTED = ["abcsd\n", "asdbc\n", "azeazez\n"]


def test_cas_simple_fichier_local(fichier_temporaire, tmp_path, dao: LectureFichierDAO):
    """Cas simple : lecture d'un fichier local créé inline"""

    lignes = list(
        dao.lire_lignes(base_dir=tmp_path, chemin_fichier_str=PATH_FICHIER_DE_TEST)
    )

    assert lignes == EXPECTED


# ou plutôt dans une classe
@pytest.mark.usefixtures("fichier_temporaire")
class TestLireLigneFichierLocal:
    """
    Ici le test n'est plus unitaire, il devient fonctionnel, car on effectue réellement l'action et on crée réellement un fichier
    """

    def test_cas_simple_fichier_local(
        self, fichier_temporaire, tmp_path, dao: LectureFichierDAO
    ):
        """Cas simple : lecture d'un fichier local créé inline"""

        lignes = list(
            dao.lire_lignes(base_dir=tmp_path, chemin_fichier_str=PATH_FICHIER_DE_TEST)
        )

        assert lignes == EXPECTED


# On peut également mocker des appels, c'est à dire contrôler de l'extérieur le fonctionnement
# Dans pytest, on utilise des **mocker** via la dépendance pytest-mock, c'est une fixture par défaut également
# Cela offre une meilleure robustesse, une isolation mais également quelques contrecoups si on estime mal le comportement de la librairie copiée


class TestLireLigneFichierDistant:
    def test_lire_lignes_remote_file_mocking_requests(
        self, dao: LectureFichierDAO, mocker
    ):
        """
        Ici on va tester la fonction _lire_lignes_remote_file
        Cette fonction est appellée dans lire_lignes_remote_file
        Il faut garder en tête qu'on ne pourra pas tout tester et donc focus les fonctions que l'on
        met a disposition pour les autres modules, les fonctions publiques
        """

        mock_response = (
            mocker.Mock()
        )  # on peut "annuler les appels à différentes fonction"
        mock_response.raise_for_status = (
            mocker.Mock()
        )  # comme celle qui controle le status HTTP de la requete
        mock_response.iter_lines = mocker.Mock(return_value='{"data": "ok"}')

        mocker.patch("requests.get", return_value=mock_response)

        # Act
        lignes = list(
            dao.lire_lignes(
                base_dir="", chemin_fichier_str="https://api.example.com/data"
            )
        )

        # Assert
        assert lignes == [
            "{",
            '"',
            "d",
            "a",
            "t",
            "a",
            '"',
            ":",
            " ",
            '"',
            "o",
            "k",
            '"',
            "}",
        ]
