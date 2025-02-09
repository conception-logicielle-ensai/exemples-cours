import json

# Données à sauvegarder
data = {"utilisateurs": [{"nom": "Alice", "age": 30}, {"nom": "Bob", "age": 25}]}

# Écriture dans un fichier JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Lecture du fichier JSON
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)