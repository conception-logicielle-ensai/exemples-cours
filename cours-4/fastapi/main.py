from fastapi import FastAPI
from controllers.item_controller import router as item_router

app = FastAPI()

# Inclure les routes de l'article
app.include_router(item_router, prefix="/items")  

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'application FastAPI!"}
