from django.db import models

class ActualWeather(models.Model):
    city_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.city_name} - {self.date_time}"
    
class Forecast(models.Model):
    city_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)