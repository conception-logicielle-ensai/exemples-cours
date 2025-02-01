from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers.recipe_router import router as recipe_router 

app = FastAPI()

# Monter le dossier des fichiers statiques
app.mount("/static", StaticFiles(directory="static"), name="static")

# Inclure le router pour les recettes
app.include_router(recipe_router)

# Vous pouvez garder ici une route pour la page d'accueil, par exemple
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, error: str = None):
    return templates.TemplateResponse("index.html", {"request": request, "error": error})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)