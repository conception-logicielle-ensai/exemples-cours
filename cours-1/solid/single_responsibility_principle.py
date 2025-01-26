# Mauvaise pratique : une seule classe gère plusieurs responsabilités.
class Order:
    def calculate_total(self):
        pass  # Calcul du total
    def print_order(self):
        pass  # Imprime la commande
    def save_to_db(self):
        pass  # Sauvegarde dans la base de données

# Bonne pratique : chaque classe gère une seule responsabilité.
class Order:
    def calculate_total(self):
        pass

class OrderPrinter:
    def print_order(self, order):
        pass

class OrderRepository:
    def save_to_db(self, order):
        pass