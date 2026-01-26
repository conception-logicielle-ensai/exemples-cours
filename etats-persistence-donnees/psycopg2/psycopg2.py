import psycopg2
import os

# Création de la table si elle n'existe pas
def initdb(conn,cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id SERIAL PRIMARY KEY,
        nom TEXT,
        age INTEGER,
        ville TEXT
    )
    ''')
    conn.commit()

class User:
    id: str  # Identifiant bdd non récupéré sauf en cas de requête SQL
    nom: str
    age: int
    ville: str

    def __init__(self, id: str, nom: str, age: int, ville: str):
        self.id = id
        self.nom = nom
        self.age = age
        self.ville = ville

    @classmethod
    def from_data(cls, data: dict):
        return User(None, data["nom"], data["age"], data["ville"])

    @classmethod
    def from_sql_result(cls, data: tuple):
        if data is None:
            return None
        return User(data[0], data[1], data[2], data[3])

    def __str__(self):
        return f"User : id {self.id}, nom {self.nom}, age {self.age}, ville {self.ville}"

# CREATE (Insertion)
def create_user(cursor, conn, user: User):
    cursor.execute('''
    INSERT INTO user_data (nom, age, ville)
    VALUES (%s, %s, %s)
    ''', (user.nom, user.age, user.ville))
    conn.commit()

# READ (Sélection)
def read_where_nom(cursor, where_nom: str) -> User:
    cursor.execute('''
    SELECT * FROM user_data WHERE nom = %s
    ''', (where_nom,))
    resultat_raw_sql = cursor.fetchone()
    return User.from_sql_result(resultat_raw_sql)

def update_user_set_age_where_nom(cursor, conn, age: int, nom: str):
    cursor.execute('''
    UPDATE user_data
    SET age = %s
    WHERE nom = %s
    ''', (age, nom))
    conn.commit()

def delete_user_where_nom(cursor, conn, nom: str):
    # DELETE (Suppression)
    cursor.execute('''
    DELETE FROM user_data WHERE nom = %s
    ''', (nom,))
    conn.commit()


# Configuration de la base de données PostgreSQL
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "postgres")  
DB_USER = os.getenv("DB_USER", "postgres")  
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")  

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()

initdb(conn, cursor)

user_data = {
    "nom": "John",
    "age": 30,
    "ville": "Paris"
}
user = User.from_data(user_data)  # Privilégiez de passer par un objet unique qui wrappe des constructeurs
print(user)
create_user(cursor, conn, user)
found_user = read_where_nom(cursor, "John")
print(found_user)
update_user_set_age_where_nom(cursor, conn, age=31, nom="John")
updated_user = read_where_nom(cursor, "John")
print(f"Mise à jour de l'age : {updated_user.age} par rapport à {found_user.age}")
delete_user_where_nom(cursor, conn, "John")
deleted_user = read_where_nom(cursor, "John")
print(deleted_user)

# Fermeture de la connexion
conn.close()
