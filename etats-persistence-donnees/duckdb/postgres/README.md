# Duckdb Postgres

Ce petit exemple vous permet de voir comment utiliser duckdb pour se connecter a une bdd postgresql.

**MAIS QUELLE BASE?**

=> Nous allons la mettre en place via docker
```sh
sudo docker build -t duckdb-postgres-demo .
sudo docker run -p 5432:5432 --name pg-demo duckdb-postgres-demo
```

Après ces commandes une bdd est disponible ici : 
```sh
postgresql://demo:demo@localhost:5432/demo_db
```

Enfin la base tournant, on peut lancer notre script:
```sh
uv sync
uv run main.py
```