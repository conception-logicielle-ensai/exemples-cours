from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import os
from urllib.parse import urlparse
import time

# Configuration
pdf_folder = "dist" # je choisis de creer le dossier dist non versionné
os.makedirs(pdf_folder, exist_ok=True)

# Options Chrome
options = Options()
#otions.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

def construction_des_pdfs(path:str):
    try:
        # 1 on récupère la page principale listant les cours
        driver.get("https://conception-logicielle.abrunetti.fr/cours")
        
        # Attendre que la page soit chargée
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "a"))
        )
        
        # 2. on récupère tous les liens (balise a en html)
        links = []
        elements = driver.find_elements(By.TAG_NAME, "a")
        
        for el in elements:
            try:
                href = el.get_attribute("href")
                if href and urlparse(href).path.startswith("/cours"):
                    if href not in links:  # On filtre pour éviter les doublons
                        links.append(href)
            except Exception as e:
                print(f"Erreur lors de la récupération d'un lien : {e}")
                continue
        
        print(f"Nombre de pages trouvées : {len(links)}")
        
        # On génère les fichiers de sortie a partir des liens trouvés
        for i, url in enumerate(links, 1):
            try:
                print(f"Traitement de la page {i}/{len(links)} : {url}")
                driver.get(url)
                
                # Attendre le chargement du contenu
                time.sleep(3)
                
                # Générer un PDF via DevTools Protocol (Chrome uniquement)
                result = driver.execute_cdp_cmd("Page.printToPDF", {
                    "printBackground": True,
                    "landscape": False,
                    "paperWidth": 8.27,  # A4
                    "paperHeight": 11.69,
                    "marginTop": 0.4,
                    "marginBottom": 0.4,
                    "marginLeft": 0.4,
                    "marginRight": 0.4,
                    "preferCSSPageSize": True
                })
                
                pdf_data = base64.b64decode(result['data'])
                
                # Créer un nom de fichier basé sur l'URL
                page_name = urlparse(url).path.replace("/cours/", "").replace("/", "_")
                if not page_name:
                    page_name = f"page_{i:02d}"
                
                pdf_path = os.path.join(pdf_folder, f"{i:02d}_{page_name}.pdf")
                
                with open(pdf_path, "wb") as f:
                    f.write(pdf_data)
                
                print(f"✓ PDF généré : {pdf_path}")
                
            except Exception as e:
                print(f"✗ Erreur lors du traitement de {url} : {e}")
                continue

    except Exception as e:
        print(f"Erreur générale : {e}")

    finally:
        driver.quit()
        print(f"\nTerminé ! {len(os.listdir(pdf_folder))} PDFs générés dans le dossier '{pdf_folder}'")

def fusion_pdf(path:str):
    from PyPDF2 import PdfMerger
    merger = PdfMerger()
    pdf_files = sorted([f for f in os.listdir(path) if f.endswith('.pdf')])
        
    for pdf_file in pdf_files:
        pdf_path = os.path.join(path, pdf_file)
        merger.append(pdf_path)
        print(f"Ajout de {pdf_file}")
        
    output_path = "dist/cours_complet.pdf"
    merger.write(output_path)
    merger.close()
        
    print(f"\n✓ PDF complet créé : {output_path}")

construction_des_pdfs(pdf_folder)
fusion_pdf(pdf_folder)