import re
import requests

def extract_with_regex(html, pattern):
    """
    Récupération de toutes les données correspondant à un pattern regex
    """
    matches = re.findall(pattern, html, re.DOTALL)
    return [match.strip() for match in matches]

# Tous les titres
pattern_titre_cours = r"<h2>(.*?)</h2>"

# Titres commençant par A
pattern_titre_cours_commencant_par_a = r"<h2>(A.*?)</h2>"

URL_COURS = "https://conception-logicielle.abrunetti.fr/cours/"
response = requests.get(URL_COURS)
html = response.text

titre_cours = extract_with_regex(html, pattern_titre_cours)
titre_cours_commencant_par_a = extract_with_regex(html, pattern_titre_cours_commencant_par_a)

print("Tous les titres :", titre_cours)
# Tous les titres : ['Git Avancé', 'Architecture applicative', 'Gestionnaire de package, partage de code, industrialisation', "Configuration du code en fonction de l'environnement", 'Bonnes pratiques du développement et design patterns', "Outils d'analyse statique d'une base de code", "Analyse dynamique d'une base de code", 'Automatisation des contrôles sur une base de code versionnée', "HTTP: Consommation et construction d'API webservice", 'Récupération de données via le webscraping']
print("Titres commençant par A :", titre_cours_commencant_par_a)
# Titres commençant par A : ['Architecture applicative', "Analyse dynamique d'une base de code", 'Automatisation des contrôles sur une base de code versionnée']