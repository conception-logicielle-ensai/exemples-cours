# On part d'un environnement ubuntu 22.04, connu.
FROM ubuntu:22.04
# on installe python comme sur un ubuntu (les commandes du début du cours)
RUN apt-get update && apt-get install -y python3-pip
# On copie les fichier de notre projet dans l'environnement
COPY . .
# On installe les dépendances du fichier requirements.txt qui est dans notre projet dans l'image 
# a partir du pip qui est dans le projet 
# et du fichier requirements qu'on vient de copier
RUN pip install -r requirements.txt
# On précise la commande a lancer pour lancer notre application depuis la racine de notre projet
CMD ["python","main.py"]