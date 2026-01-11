from fastapi import HTTPException, FastAPI
from typing import List

from pydantic import BaseModel, Field

app = FastAPI()

import sqlite3
from typing import Optional, Literal

class Singleton(type):
    """ A metaclass that creates a Singleton base class when called. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnector(metaclass=Singleton):
    _connection = None

    def __init__(self, db_type: Literal['sqlite'] = 'sqlite', 
                 db_name: Optional[str] = 'default.db'):
        self.db_type = db_type
        self.db_name = db_name
        self.connect()       
    def _connect_sqlite(self, db_name):
        try:
            DatabaseConnector._connection = sqlite3.connect(db_name)
        except sqlite3.Error as e:
            print(f"Erreur de connexion SQLite : {e}")

    def connect(self):
        if DatabaseConnector._connection is not None:
            raise RuntimeError("Base de données déjà connectée!")
        
        if self.db_type == 'sqlite':
            self._connect_sqlite(self.db_name)
        else:
            raise ValueError("Type de base de données inconnu. Choisissez 'sqlite' ou '?'.")
 
    def init_db(self):
        if self.db_type == 'sqlite':
            connexion = self.get_connection()
            cursor = connexion.cursor()
            # creation table users
            cursor.execute('''DROP TABLE IF EXISTS users;''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL
                    );''')
            cursor.execute('''DROP TABLE IF EXISTS roles_users;''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS roles_user (
                        user_id INTEGER NOT NULL,
                        role TEXT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users (id)
                    );''')
            connexion.commit()
            # Insertion d'un utilisateur 'admin'
            cursor.execute("INSERT INTO users (username) VALUES (?)", ("adm",))
            user_id = cursor.lastrowid  # Récupère l'id du nouvel utilisateur
            # Insertion du rôle 'admin' pour cet utilisateur
            cursor.execute("INSERT INTO roles_user (user_id, role) VALUES (?, ?)", (user_id, "admin"))
            cursor.execute("INSERT INTO roles_user (user_id, role) VALUES (?, ?)", (user_id, "dev"))
            connexion.commit()
            user_id = cursor.lastrowid 
            cursor.execute("INSERT INTO users (username) VALUES (?)", ("pasadm",))
            cursor.execute("INSERT INTO roles_user (user_id, role) VALUES (?, ?)", (user_id, "dev"))
             # Commit des changements
            connexion.commit()
            self.close_connection()

    def get_connection(self):
        if DatabaseConnector._connection is None:
            self.connect()
        return DatabaseConnector._connection
    def close_connection(self):
        """ Ferme la connexion à la base de données si elle est ouverte. """
        if DatabaseConnector._connection is not None:
            DatabaseConnector._connection.close()
            DatabaseConnector._connection = None

# --- Entité métier ---
class UserDTO(BaseModel):
    username: str = Field(examples=["adm","pasadm"])
    def to_user(self):
        """Convert DTO to a plain User object."""
        return User(
            id=None,
            username=self.username,
            roles=None
        )
class User:
    def __init__(self, id: Optional[str], username: str, roles: Optional[List[str]]):
        self.id = id
        self.username = username
        self.roles = roles
    def __str__(self):
        return f"User(username={self.username},roles={self.roles})"
    def __repr__(self):
        return f"User(username={self.username}, roles={self.roles})"
    def is_admin(self):
        return "admin" in self.roles

class UserDAO:
    def __init__(self, database_connector:DatabaseConnector):
        self.database_connector = database_connector
    def get_user_by_username(self, username:str ) :
        connexion = self.database_connector.get_connection()
        cursor = connexion.cursor() 
        cursor.execute("SELECT * FROM users a WHERE username = ?", (username,))
        user_dict = cursor.fetchone()
        if user_dict is None:
            raise ValueError(f"Pas d'utilisateur avec username {username}")
        cursor.execute("SELECT role from roles_user where user_id = ?",(str(user_dict[0])))
        roles = cursor.fetchall()
        distinct_roles = list(set(role[0] for role in roles))
        user = User(id=user_dict[0], username=user_dict[1],roles=distinct_roles)
        self.database_connector.close_connection()
        return user
    def save_user(self, name: str, email: str) -> int:
        cursor = self._conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self._conn.commit()
        return cursor.lastrowid
#
# --- Méthode décorée ---
class UserService:
    def __init__(self, user_dao:UserDAO):
        self.user_dao = user_dao
    def peut_se_connecter(self,user: User):
        """Vérifie si l'utilisateur peut se connecter (uniquement pour les administrateurs)."""
        print(user)
        if user.is_admin():
            return {"message": f"User {user.username} can connect as admin."}
        return {"message": f"User {user.username} cannotconnect as admin."}
    def get_user(self,user_dto:UserDTO):
        user = user_dto.to_user()
        updated_user = self.user_dao.get_user_by_username(user.username)
        return updated_user 
# --- API Endpoint ---
@app.post("/connect")
def connect(user_dto: UserDTO):
    """
    Endpoint qui utilise la méthode `peut_se_connecter` pour vérifier si l'utilisateur peut accéder.
    Un utilisateur avec le rôle "admin" est nécessaire.
    """
    user_dao = UserDAO(database_connector=DatabaseConnector())
    user_service = UserService(user_dao=user_dao)
    try:
        user = user_service.get_user(user_dto=user_dto)
        return user_service.peut_se_connecter(user=user)
    except ValueError as e:
        raise HTTPException(404,str(e))

if __name__ == "__main__":
    import uvicorn
    # initialisation du connector
    database_connector = DatabaseConnector("sqlite","default.db")
    # initialisation de la bdd : schema et donnees
    database_connector.init_db()
    # Run server
    uvicorn.run(app, host="0.0.0.0", port=8000)