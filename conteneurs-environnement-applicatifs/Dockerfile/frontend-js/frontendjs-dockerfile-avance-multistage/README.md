# FrontendJs dockerfile avancé

Ici on s'appuie sur la notion de multistage build, on construit un livrable dans un environnement qui contient tout et on le dépose dans un serveur qui a le moins de dépendances possibles, c'est le mode standard et clean de déploiement.

https://docs.docker.com/build/building/multi-stage/


Lancez moi:
```sh
sudo docker run -p 3000:80 ragatzino/frontendjs-dockerfile-avance-multistage
```

Consultez le Dockerfile.