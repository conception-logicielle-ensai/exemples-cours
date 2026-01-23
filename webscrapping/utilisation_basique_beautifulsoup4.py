from bs4 import BeautifulSoup
import requests

url = "https://conception-logicielle.abrunetti.fr/cours/"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, "html.parser")

titres = [h2.get_text(strip=True) for h2 in soup.select("article h2")]
print(titres)

links = [a["href"] for a in soup.find_all("a", href=True)]
print(links)