from src.model.compteur import Compteur

"""
Pour le compteur et les model, en général on est plus sur des tests unitaires ou des tests "fonctionnels" sur un ensemble métier
L'avantage c'est le faible nombre de dépendances du module
La stratégie ici, est de regrouper les fonctionnalités par classe, puis tester différents cas qui permettent de limiter la casse.
Encore une fois, on peut tout tester mais déjà voir l'essentiel et ne pas tester en double, c'est pas mal.
Par exemple je choisis de ne tester que le comptage de lettre, pour moi il y a plus de complexité et donc plus de valeur au test.
"""

class TestCompteurComptageParLettre:
    def test_comptage_par_lettres_emptylist_should_return_empty_count(self):
        compteur = Compteur([])
        assert compteur.comptage_par_lettre == {}
    def test_comptage_par_lettres_case_majuscules_minuscule_should_return_distinct_count(self):
        compteur = Compteur(["a","A","a","b"])
        assert compteur.comptage_par_lettre == {'A': 1, 'a': 2, 'b': 1}
    
    def test_comptage_par_lettres_case_accent_num_symbole_should_return_empty_count(self):
        compteur = Compteur(["à","$","*","23"])
        assert compteur.comptage_par_lettre == {}