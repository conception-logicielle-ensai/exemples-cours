import requests
EXAMPLE_ORG_URL = "https://example.org"
response = requests.get(EXAMPLE_ORG_URL)
print("code retour de la requête :")
print(response.status_code)
if response.status_code != response.ok:
    print("la réponse est d'un code retour qui signifie un bon fonctionnement")
print("La requete contient-t-elle du texte ?")
try:
    texte = response.text
    print("oui")
    print(texte)
except Exception as e:
    print("non")
print("La page renvoie-t-elle du json ?")
try:
    json = response.json()
    print("oui")
    print(json)
except Exception as e:
    print("non")
