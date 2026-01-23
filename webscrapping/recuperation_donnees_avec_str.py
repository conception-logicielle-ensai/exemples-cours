import requests

H2_OPEN_TAG = "<h2>"
H2_CLOSE_TAG = "</h2>"

LEN_H2_OPEN = len(H2_OPEN_TAG)
LEN_H2_CLOSE = len(H2_CLOSE_TAG)


def extraction_noms_cours_raw(html: str) -> list[str]:
    """
    Extrait les titres des cours depuis les balises <h2> contenues
    dans les <article>.
    Parsing volontairement naïf basé sur les chaînes.
    """

    titres: list[str] = []
    position = 0

    while True:
        h2_start = html.find(H2_OPEN_TAG, position)
        if h2_start == -1:
            break

        h2_end = html.find(H2_CLOSE_TAG, h2_start)
        if h2_end == -1:
            break

        titre = html[
            h2_start + LEN_H2_OPEN :
            h2_end
        ].strip()

        titres.append(titre)

        position = h2_end + LEN_H2_CLOSE

    return titres

# Exemple d’utilisation
URL_COURS = "https://conception-logicielle.abrunetti.fr/cours/"
response = requests.get(URL_COURS)
html = response.text
print(extraction_noms_cours_raw(html))
# ['Git Avancé', 'Architecture applicative', 'Gestionnaire de package, partage de code, industrialisation', "Configuration du code en fonction de l'environnement", 'Bonnes pratiques du développement et design patterns', "Outils d'analyse statique d'une base de code", "Analyse dynamique d'une base de code", 'Automatisation des contrôles sur une base de code versionnée', "HTTP: Consommation et construction d'API webservice", 'Récupération de données via le webscraping']