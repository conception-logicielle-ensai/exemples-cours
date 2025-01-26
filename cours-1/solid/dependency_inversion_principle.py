# Mauvaise pratique : dépendance directe sur une implémentation.
class Database:
    def connect(self):
        print("Connexion à la base de données...")

class UserRepository:
    def __init__(self):
        self.db = Database()
    def get_user(self, user_id):
        self.db.connect()
        print(f"Récupération de l'utilisateur {user_id}")

# Bonne pratique : dépendance sur une abstraction.
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connexion à MySQL...")

class UserRepository:
    def __init__(self, db: Database):
        self.db = db
    def get_user(self, user_id):
        self.db.connect()
        print(f"Récupération de l'utilisateur {user_id}")

# Utilisation
db = MySQLDatabase()
repo = UserRepository(db)
repo.get_user(1)

## Note les implémentations ne sont pas fidèles aux cas réels, mais sont là pour mettre en exergue le principe d'inversion de dépendance