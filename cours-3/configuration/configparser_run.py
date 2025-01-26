import configparser

# Création d'un objet ConfigParser
config = configparser.ConfigParser()

# Lecture du fichier config.ini
config.read('config.ini')

# Exemple d’accès aux données
server_interval = config['DEFAULT']['ServerAliveInterval']
user = config['forge.example']['User']
print(server_interval)  # Affiche : 45
print(user)             # Affiche : hg
