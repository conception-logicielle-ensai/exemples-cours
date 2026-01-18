# Exemple locust

Application pour montrer le concept de test de charge

## Installer le setup local
```
uv sync --dev
```

Ensuite on s'appuie sur `tox`, on pourrait également s'appuyer sur `MAKE` (renseignez vous, c'est simple mais c'est cool)

ça permet de faire tout un setup qu'on peut lancer tout simplement: 
```
uv run tox -e load-test
```


**C'est tout !** Cette commande :
1. ✅ Lance automatiquement l'API FastAPI
2. ✅ Ouvre l'interface web Locust sur http://localhost:8089
3. ✅ Démarre automatiquement les tests de charge (50 utilisateurs)
4. ✅ Affiche les statistiques en temps réel

**📊 Visualisez en direct :**
- Interface Locust : http://localhost:8089
- Documentation API : http://localhost:8000/docs

