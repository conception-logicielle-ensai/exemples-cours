from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": f"Bienvenue sur FastAPI avec SSR sur ROOT!"})

@app.get("/{chemin}", response_class=HTMLResponse)
async def home(request: Request,chemin:str):
    return templates.TemplateResponse("index.html", {"request": request, "message": f"Bienvenue sur FastAPI avec SSR {chemin}!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)