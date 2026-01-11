from typing import Callable

import pytest


class CacheManager:

    """
    classe simple qui permet, de stocker des résultats
    """
    def __init__(self):
        self.cache = {}

    def get_in_cache_else_return(self,function:Callable, function_name, *args,**kwargs):
        """
        Appelle une fonction si son nom et l'argument précisé n'a pas déjà été utilisé
        Sinon va chercher dans le dictionnaire Cache la valeur stockée lors d'un précédent appel de fonction
        """
        cache_key=f"{function_name}-{args}-{kwargs}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        else:
            self.cache[cache_key] = function(args,kwargs)
        return self.cache[cache_key]

# On créer une fonction "fixture" qui nous permet de générer une fonction qu'on pourrait injecter a la place d'une autre.
@pytest.fixture
def mock_function():
    """
    Fonction qui instancie un compteur au niveau global
    """
    count = 0
    def counter(*args,**kwargs):
        nonlocal count
        count += 1
        return count
    return counter

# On l'utilise pour verifier qu'on utilise bien le cache
def test_cache(mock_function):
    cache_manager = CacheManager()
    assert(1 == cache_manager.get_in_cache_else_return(mock_function,"mock_func",None,None))
    assert(1 == cache_manager.get_in_cache_else_return(mock_function, "mock_func", None,None))
    # Deuxieme vrai appel de la fonction
    assert(mock_function()== 2)
    # Troisieme vrai appel de la fonction
    assert(mock_function()== 3)