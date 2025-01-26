from typing import Callable


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

cache_manager = CacheManager()

from unittest import TestCase
from unittest.mock import Mock

class TestCache(TestCase):
    def test_cache_manager_ok(self):
        """
        creation d'une mock fonction qui renvoie 1 puis 2 et verification que ça renvoie 2 fois 1
        """
        mock_function = Mock(side_effect=[1,2])
        cache_manager = CacheManager()
        self.assertEqual(1,cache_manager.get_in_cache_else_return(mock_function,"mock_func",None,None))
        self.assertEqual(1,cache_manager.get_in_cache_else_return(mock_function, "mock_func", None,None))