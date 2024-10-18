import requests
import logging
from django.shortcuts import render
from django.conf import settings

logger = logging.getLogger(__name__)

def index(request):
    api_key = settings.API_KEY
    city = request.GET.get('city', 'London')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        
        context = {
            'city': city,
            'weather': weather_data['weather'][0]['description'],
            'temperature': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'pressure': weather_data['main']['pressure'],
            'wind_speed': weather_data['wind']['speed'],
            'error': None,
        }
    except requests.exceptions.HTTPError:
        logger.error(f"HTTP error occurred for city: {city}")
        context = {
            'city': city,
            'error': 'City not found. Please enter a valid city name.',
        }
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        context = {
            'city': city,
            'error': f'An error occurred: {e}',
        }

    return render(request, 'weather_app/index.html', context)