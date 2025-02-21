import os

from fastapi import FastAPI

from config.app_config import add_cors_middleware
from dao.configuration.database_connector import DatabaseConnector
from web.user_router import user_router

app = FastAPI()

app.include_router(user_router)

# Configuration CORS
add_cors_middleware(app)

if __name__ == "__main__":
    import uvicorn

    # initialisation du connector
    database_connector = DatabaseConnector(
        db_type=os.getenv("DB_TYPE", "postgres"),
        db_name=os.getenv("DB_NAME", ""),
        user=os.getenv("DB_USER", ""),
        password=os.getenv("DB_PASSWORD", ""),
        host=os.getenv("DB_HOST", ""),
        port=int(os.getenv("DB_PORT", 0)),
    )  # Port doit être un int
    # initialisation de la bdd : schema et donnees
    database_connector.init_db()
    # Run server
    uvicorn.run(app, host="0.0.0.0", port=8000)
