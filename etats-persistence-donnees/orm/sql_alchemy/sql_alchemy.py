import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from typing import Literal

def get_instance(instance_type: Literal["postgres", "sqlite"]) -> str:
    """
    Renvoie l'URL de connexion pour la base de données en fonction du type de base.
    
    :param instance_type: Le type de base de données, soit "postgres", soit "sqlite".
    :return: L'URL de connexion correspondante.
    """
    if instance_type == "postgres":
        # Construction de l'URL pour PostgreSQL
        # Configuration de la base de données PostgreSQL
        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_NAME = os.getenv("DB_NAME", "postgres")  
        DB_USER = os.getenv("DB_USER", "postgres")  
        DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")  
        
        # Connexion à la base de données PostgreSQL avec SQLAlchemy
        PG_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
        # Construction de l'URL PostgreSQL
        return PG_DATABASE_URL
    elif instance_type == "sqlite":
        DB_PATH = os.getenv("DB_PATH", "database.db")
        return f"sqlite:///{DB_PATH}"
    else:
        raise ValueError(f"Type de base de données non supporté : {instance_type}")

instance_type = os.getenv("DB_INSTANCE_TYPE","sqlite")   
bdd_instance = get_instance(instance_type)

# Création de l'objet Engine
engine = create_engine(bdd_instance, echo=True)

# Base déclarative
Base = declarative_base()

# Définition de la classe User (Table)
class User(Base):
    __tablename__ = 'user_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String, nullable=False)
    age = Column(Integer)
    ville = Column(String)

    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def __repr__(self):
        return f"User(id={self.id}, nom={self.nom}, age={self.age}, ville={self.ville})"

def initDb(base):
    # Créer la table dans la base de données
    base.metadata.create_all(engine)



# CREATE (Insertion)
def create_user(session, user: User):
    session.add(user)
    session.commit()

# READ (Sélection)
def read_where_nom(session, where_nom: str) -> User:
    return session.query(User).filter(User.nom == where_nom).first()

# UPDATE (Mise à jour)
def update_user_set_age_where_nom(session, nom: str, age: int):
    user = session.query(User).filter(User.nom == nom).first()
    if user:
        user.age = age
        session.commit()

# DELETE (Suppression)
def delete_user_where_nom(session, nom: str):
    user = session.query(User).filter(User.nom == nom).first()
    if user:
        session.delete(user)
        session.commit()
# Session
Session = sessionmaker(bind=engine)
session = Session()
# Exemple d'utilisation
user_data = {
    "nom": "John",
    "age": 30,
    "ville": "Paris"
}
user = User(**user_data)  # Créer un objet User
print(user)
create_user(session, user)  # Ajouter à la base de données
found_user = read_where_nom(session, "John")
print(found_user)
update_user_set_age_where_nom(session, "John", 31)
updated_user = read_where_nom(session, "John")
print(f"Mise à jour de l'age : {updated_user.age} par rapport à {found_user.age}")
delete_user_where_nom(session, "John")
deleted_user = read_where_nom(session, "John")
print(deleted_user)

# Fermeture de la session
session.close()