class Pokemon:
    def __init__(self, id_, name, weight, height, types, stats, sprite):
        self.id = id_
        self.name = name
        self.weight = weight
        self.height = height
        self.types = types
        self.stats = stats  # Dictionnaire des statistiques de base (HP, Attaque, Défense, etc.)
        self.sprite = sprite  # URL de l'image du Pokémon

    def __str__(self):
        stats_str = "\n".join([f"{key.capitalize()}: {value}" for key, value in self.stats.items()])
        types_str = ", ".join(self.types)
        return (f"Pokémon: {self.name.upper()} (#{self.id})\n"
                f"Weight: {self.weight}\n"
                f"Height: {self.height}\n"
                f"Types: {types_str}\n"
                f"Stats:\n{stats_str}\n"
                f"Sprite: {self.sprite}")
