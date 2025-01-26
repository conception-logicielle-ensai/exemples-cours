# Mauvaise pratique : modification du code existant pour ajouter un comportement.
class Discount:
    def apply_discount(self, price, discount_type):
        if discount_type == "percentage":
            return price * 0.9
        elif discount_type == "fixed":
            return price - 10

# Bonne pratique : extension via des classes dérivées.
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class PercentageDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.9

class FixedDiscount(Discount):
    def apply_discount(self, price):
        return price - 10