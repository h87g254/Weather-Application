from django.db import models
from django.utils import timezone
from datetime import timedelta

class CityWeather(models.Model) :
    city = models.CharField(max_length=100)
    weather = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def is_recent(self):
        return timezone.now() - self.timestamp < timedelta(minutes=5)