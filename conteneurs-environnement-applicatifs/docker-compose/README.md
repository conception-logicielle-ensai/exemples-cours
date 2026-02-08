# Documentation exemple de docker compose pour une application qui a un dossier backend et un dossier frontend


Vous pouvez lancer l'application en local directement avec la commande : 
```sh
sudo docker compose up
```

Vous pouvez également travailler en lançant certains modules : 
- Pour travailler sur l'UI:
```sh
sudo docker compose up db backend
```

- Pour travailler sur l'API, lancer la BDD:
```sh
sudo docker compose up db
```

Vous pouvez les arrêter avec 

```sh
sudo docker compose down
```