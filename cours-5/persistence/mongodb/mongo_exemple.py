from pymongo import MongoClient
import os

MONGO_HOSTS=os.getenv("MONGO_HOST","localhost:27017")
MONGO_DB=os.getenv("MONGO_DB","defaultdb")
client = MongoClient(f'mongodb://{MONGO_HOSTS}/{MONGO_DB}')
db=client.defaultdb



def create(collection,document:dict):
    collection.insert_one(document)


def read(collection,filtre:dict):
    resultat = collection.find_one(filter=filtre)
    return resultat
def update(collection,filtre:dict,filtre_update:dict) -> dict:

    collection.update_one(filter=filtre,update=filtre_update)
    updated = collection.find_one(filtre)
    return updated

def delete(collection,filtre):
    collection.delete_one(filter=filtre)

COLLECTION = "user_data"
collection = db[COLLECTION]  # Remplacez par le nom de votre collection

# Exemple d'insertion d'un document dans la collection
document = {
    "nom": "John",
    "age": 30,
    "ville": "Paris"
}

create(collection=collection,document=document)
filtre = {"nom": "John"} # equivalent du where en sql
found_document = read(collection=collection,filtre=filtre)
print(found_document)
filtre_update = {"$set": {"age":"31"}} # equivalent du set where en sql
updated = update(collection,filtre,filtre_update)
print(f"Mise a jour de l'age : {updated["age"]} par rapport a {found_document["age"]}")
delete(collection,filtre=filtre)
element_apres_suppression = read(collection,filtre)
print(element_apres_suppression)