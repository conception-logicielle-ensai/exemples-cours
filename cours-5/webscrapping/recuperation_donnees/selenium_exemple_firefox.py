from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Initialisation du navigateur avec Selenium (utilisation de Firefox et Geckodriver)
#options = webdriver.FirefoxOptions()
#options.add_argument("--headless")  # Exécuter en mode background (optionnel)
driver = webdriver.Firefox(
    #options=options
)  # Utilisation de Firefox au lieu de Chrome
JUST_WATCH_URL = "https://www.justwatch.com"
def search(movie_name):
    """
    Effectue la recherche du champ movie_name dans la barre de recherche du site
    => Atterit sur la page du site
    """
    search_box = driver.find_element(By.CSS_SELECTOR, "input.search-bar__input")  # Le champ de recherche
    search_box.click()
    search_box.send_keys(movie_name + Keys.ENTER)
    time.sleep(10)  # Attendre les résultats
    film_title = driver.find_element(By.CLASS_NAME,"header-title")
    if film_title.text.lower() == movie_name.lower():
        print(f"Le film {movie_name} est bien disponible sur la plateforme")
    else:
        raise Exception("Le film n'existe pas après la recherche")
    #film_click = driver.find_element(By.CLASS_NAME,"title-list-row__column-header")
    #film_click.click()
    
def get_projections_ou_plateformes(movie_name:str):
    """
    Depuis la page de recherche, récupère les sous liens
    """
    platforms = driver.find_elements(By.CSS_SELECTOR, ".buybox-row__offers .offer")  # Trouver les projections_ou_plateformes

    if platforms:
        print(f"Le film '{movie_name}' est disponible, liens:")
        for platform in platforms:
            print(" - "+platform.get_attribute("href"))  # Affiche chaque plateforme
    else:
        print(f"Désolé, aucun résultat trouvé pour le film '{movie_name}'.")
def accepter_cookies() -> bool:
    """
    Accepte les cookies si popup
    """

    # On accède a un shadow dom
    shadow_host = driver.find_element(By.CSS_SELECTOR, '#usercentrics-root')  # Change ce sélecteur si nécessaire

    # Accéder au shadow root
    shadow_root = shadow_host.shadow_root

    # Trouver le bouton dans le shadow DOM
    try:
        cookie_accept_all = WebDriverWait(shadow_root, 6).until(
         EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="uc-accept-all-button"]'))
        )

        # Cliquer sur le bouton
        cookie_accept_all.click()
    except:
        print("aucune étape de cookie trouvée, skip...")
    time.sleep(5)  # Attendre que l'acceptation soit prise en compte
def find_movie_platform_or_projection(movie_name):
    """
    Trouver les projections_ou_plateformes sur lesquelles le film peut se regarder
    """
    try:
        driver.get(url=JUST_WATCH_URL)
        time.sleep(3)
        time.sleep(3)
        accepter_cookies()

        search(movie_name)
        # 3️⃣ Vérifier si des résultats sont trouvés et récupérer les projections_ou_plateformes
        get_projections_ou_plateformes(movie_name=movie_name) 

    except Exception as e:
        print("Erreur :", e)
    finally:
        driver.quit()  # Fermer le navigateur après l'exécution du test

# Exécution du test pour chercher un film
find_movie_platform_or_projection("Inception")