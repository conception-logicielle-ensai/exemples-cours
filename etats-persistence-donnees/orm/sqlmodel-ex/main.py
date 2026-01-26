from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from configuration.database import init_db
from routers.user_router import router

# Initialisation de la base de données au démarrage
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialisation au démarrage (fonction sync appelée dans contexte async)
    print("🚀 Démarrage de l'application...")
    init_db()
    print("✅ Base de données initialisée")
    yield
    # Cleanup au shutdown (si nécessaire)
    print("👋 Arrêt de l'application...")

app = FastAPI(title="API Gestion Utilisateurs",lifespan=lifespan)
    
# Enregistrement des routes
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "API Gestion Utilisateurs",
        "endpoints": {
            "POST /users/": "Créer un utilisateur",
            "GET /users/": "Lister tous les utilisateurs",
            "GET /users/{id}": "Obtenir un utilisateur",
            "PUT /users/{id}": "Modifier un utilisateur",
            "DELETE /users/{id}": "Supprimer un utilisateur"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
