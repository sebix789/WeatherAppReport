from django.contrib import admin
from .models import ActualWeather, Forecast

admin.site.register(ActualWeather)
admin.site.register(Forecast)
