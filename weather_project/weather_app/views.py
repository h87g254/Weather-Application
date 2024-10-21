import requests
import logging
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone
from .models import CityWeather

logger = logging.getLogger(__name__)

def index(request):
    api_key = settings.API_KEY
    city = request.GET.get('city', 'London').lower()
    
    # Check if the city data is already in the database and is recent
    city_weather = CityWeather.objects.filter(city=city).first()
    if city_weather and city_weather.is_recent():
        weather_data = {
            'weather': city_weather.weather,
            'main': {
                'temp': city_weather.temperature,
                'humidity': city_weather.humidity,
                'pressure': city_weather.pressure,
            },
            'wind': {
                'speed': city_weather.wind_speed,
            }
        }
    else:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            
            # Save the new data to the database
            CityWeather.objects.update_or_create(
                city=city,
                defaults={
                    'weather': weather_data['weather'][0]['description'],
                    'temperature': weather_data['main']['temp'],
                    'humidity': weather_data['main']['humidity'],
                    'pressure': weather_data['main']['pressure'],
                    'wind_speed': weather_data['wind']['speed'],
                    'timestamp': timezone.now()
                }
            )
        except requests.exceptions.HTTPError:
            logger.error(f"HTTP error occurred for city: {city}")
            context = {
                'city': city,
                'error': 'City not found. Please enter a valid city name.',
            }
            return render(request, 'weather_app/index.html', context)
        except requests.exceptions.RequestException as e:
            logger.error(f"Request exception occurred: {e}")
            context = {
                'city': city,
                'error': f'An error occurred: {e}',
            }
            return render(request, 'weather_app/index.html', context)

    context = {
        'city': city,
        'weather': weather_data['weather'][0]['description'],
        'temperature': weather_data['main']['temp'],
        'humidity': weather_data['main']['humidity'],
        'pressure': weather_data['main']['pressure'],
        'wind_speed': weather_data['wind']['speed'],
        'error': None,
    }

    return render(request, 'weather_app/index.html', context)