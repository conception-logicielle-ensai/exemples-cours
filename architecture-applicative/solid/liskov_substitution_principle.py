# Mauvaise pratique : la classe dérivée casse le contrat de la classe parent.
class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Les pingouins ne volent pas!")

# Bonne pratique : refactorisation pour respecter le contrat.
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("Je vole!")

class NonFlyingBird(Bird):
    def move(self):
        print("Je marche!")