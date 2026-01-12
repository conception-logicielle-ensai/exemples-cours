# Pour info, pas compatible avec toutes les versions de python, voilà la portabilité par l'exemple :)
class Sandwich:
    def __init__(self):
        self.bread:str | None = None
        self.protein:str | None = None
        self.cheese:str | None = None
        self.vegetables:list[str] = []
        self.sauces:list[str] = []
    @property
    def bread(self):
        return self._bread

    @bread.setter
    def bread(self, type_bread:str):
        self._bread = type_bread

    @property
    def protein(self):
        return self._protein

    @protein.setter
    def protein(self, type_protein: str):
        self._protein = type_protein

    @property
    def cheese(self):
        return self._cheese

    @cheese.setter
    def cheese(self, cheese_type:str):
        self._cheese = cheese_type

    @property
    def vegetables(self):
        return self._vegetables
    @vegetables.setter
    def vegetables(self, vegetables:list[str]):
        self._vegetables = vegetables
    def add_vegetable(self, vegetable:str):
        if vegetable:
            self._vegetables.append(vegetable)

    @property
    def sauces(self):
        return self._sauces
    @sauces.setter
    def sauces(self, sauces:list[str]):
        self._sauces = sauces
    def add_sauce(self, sauce:str):
        if sauce:
            self._sauces.append(sauce)

    def __str__(self):
        return (
            f"Sandwich(bread={self.bread}, protein={self.protein}, "
            f"cheese={self.cheese}, vegetables={self.vegetables}, sauces={self.sauces})"
        )

class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()

    def set_bread(self, bread:str):
        self.sandwich.bread = bread
        return self

    def set_protein(self, protein:str):
        self.sandwich.protein = protein
        return self

    def add_cheese(self, cheese:str):
        self.sandwich.cheese = cheese
        return self

    def add_vegetable(self, vegetable:list[str]):
        self.sandwich.vegetables.append(vegetable)
        return self

    def add_sauce(self, sauce:list[str]):
        self.sandwich.sauces.append(sauce)
        return self

    def build(self):
        return self.sandwich

# Exemple d'utilisation
if __name__ == "__main__":
    builder = SandwichBuilder()
    custom_sandwich = (
        builder.set_bread("Italian")
               .set_protein("Chicken Teriyaki")
               .add_cheese("Swiss")
               .add_vegetable("Lettuce")
               .add_vegetable("Tomato")
               .add_vegetable("Pickles")
               .add_sauce("Honey Mustard")
               .add_sauce("Chipotle Southwest")
               .build()
    )
    print(custom_sandwich)
    # Sandwich(bread=Italian, protein=Chicken Teriyaki, cheese=Swiss, vegetables=['Lettuce','Tomato','Pickles'], sauces=['Honey Mustard', 'Chipotle Southwest'])