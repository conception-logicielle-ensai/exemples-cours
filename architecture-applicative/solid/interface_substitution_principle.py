# Mauvaise pratique : une interface trop large.
class Animal:
    def eat(self):
        pass
    def fly(self):
        pass
    def swim(self):
        pass

class Dog(Animal):
    def eat(self):
        pass
    def fly(self):  # Non pertinent pour un chien.
        raise NotImplementedError()
    def swim(self):
        pass

dog = Dog()
try:
    dog.fly()
except NotImplementedError as e:
    print("Pour la premiere implementation, il est surprenant d'avoir une fonction qui ne fait rien")

# Bonne pratique : des interfaces spécifiques.
from abc import ABC, abstractmethod

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        pass

class Dog(Eater, Swimmer):
    def eat(self):
        print("Je mange!")
    def swim(self):
        print("Je nage!")