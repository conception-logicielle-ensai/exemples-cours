from models.item import Item

class ItemService:
    def create_item(self, item: Item) -> Item:
        # Logique pour créer l'article (par exemple, sauvegarde en base de données)
        return item

    def get_items(self) -> list[Item]:
        # Logique pour récupérer les articles (par exemple, depuis une base de données)
        return [
            Item(name="Portal Gun", price=42.0),
            Item(name="Plumbus", price=32.0),
        ]
