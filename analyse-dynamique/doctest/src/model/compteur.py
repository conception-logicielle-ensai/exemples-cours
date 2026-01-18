from functools import reduce
from typing import Counter, Dict, Iterable

from src.custom_types import Lettre


class Compteur:
    """
    Compteur de lettres par ligne.

    >>> # test 1 : liste vide
    >>> compteur = Compteur([])
    >>> compteur.comptage_par_lettre
    {}

    >>> # test 2 : majuscules et minuscules
    >>> compteur = Compteur(["a", "A", "a", "b"])
    >>> compteur.comptage_par_lettre
    {'a': 2, 'A': 1, 'b': 1}

    >>> # test 3 : accents, chiffres et symboles
    >>> compteur = Compteur(["à", "$", "*", "23"])
    >>> compteur.comptage_par_lettre
    {}
    """
    def __init__(self, lignes: Iterable[str]):
        from itertools import tee

        (
            self.__iterateur_total_lignes,
            self.__iterateur_total_caracteres,
            self.__iterateur_total_comptage_lettre,
        ) = tee(lignes, 3)

    @property
    def total_lignes(self) -> int:
        return len(
            list(filter(lambda ligne: ligne != None, self.__iterateur_total_lignes))
        )

    @property
    def total_caracteres(self) -> int:
        return sum(
            map(
                len,
                filter(lambda ligne: ligne != None, self.__iterateur_total_caracteres),
            )
        )

    def __compter_lettres_par_ligne(self):
        """
        On transforme chaque ligne (str) en Counter, type qui fait le job de lister les occurences
        """
        return list(
            map(lambda ligne: Counter(ligne), self.__iterateur_total_comptage_lettre)
        )

    def __filtrer_comptage_par_lettre_alphabetique(self, comptage: Counter):
        ALLOWED_LETTERS = set(
            [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
            ]
        )
        # ici k,v c'est assez explicite / classique
        return Counter(
            {k: v for k, v in comptage.items() if k.lower() in ALLOWED_LETTERS}
        )

    @property
    def comptage_par_lettre(self) -> Counter[Lettre]:
        counters_par_ligne = self.__compter_lettres_par_ligne()
        counters_filtres = map(
            self.__filtrer_comptage_par_lettre_alphabetique, counters_par_ligne
        )
        total_counter = reduce(lambda acc, c: acc + c, counters_filtres, Counter())
        return dict(total_counter)

    @property
    def characters_data(self):
        return {
            "nb_lignes": self.total_lignes,
            "nb_caracteres": self.total_caracteres,
            "comptage_par_lettre": self.comptage_par_lettre,
        }
