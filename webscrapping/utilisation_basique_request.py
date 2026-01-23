import requests

URL_COURS = "https://conception-logicielle.abrunetti.fr/"
response = requests.get(URL_COURS)
print(response.text)  # Affiche le contenu HTML de la page