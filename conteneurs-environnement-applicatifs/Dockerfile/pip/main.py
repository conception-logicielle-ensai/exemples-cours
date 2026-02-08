from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "weather": None, "error": None})

@app.post("/", response_class=HTMLResponse)
def get_weather(request: Request, city: str = Form(...)):
    weather_data = None
    error = None
    url = f"https://wttr.in/{city}?format=j1"  # API publique JSON

    try:
        response = requests.get(url)
        data = response.json()
        
        # Extraction simple des infos
        current = data["current_condition"][0]
        weather_data = {
            "city": city.title(),
            "temperature": current["temp_C"],
            "description": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "feels_like": current["FeelsLikeC"]
        }
    except Exception as e:
        error = f"Impossible de récupérer la météo pour {city}: {str(e)}"

    return templates.TemplateResponse("index.html", {"request": request, "weather": weather_data, "error": error})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)