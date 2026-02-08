from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import requests


@require_http_methods(["GET", "POST"])
def index(request):
    weather_data = None
    error = None
    
    if request.method == "POST":
        city = request.POST.get('city', '')
        
        if city:
            url = f"https://wttr.in/{city}?format=j1"
            
            try:
                response = requests.get(url)
                data = response.json()
                
                # Extraction des infos
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
    
    context = {
        "weather": weather_data,
        "error": error
    }
    
    return render(request, 'index.html', context)

def members(request):
    return HttpResponse("Hello world!")