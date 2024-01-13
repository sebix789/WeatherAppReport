from celery import shared_task
from django.db import connection, OperationalError
from django.utils import timezone
from .models import ActualWeather, Forecast
from weatherdbapp.celery import app
import environ
import requests

@app.task
def weather_data_fetch_and_update():
    env = environ.Env()
    environ.Env.read_env()
    API = env("API_KEY")
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Cracow&units=metric&appid={0}'.format(API)
    forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?q=Cracow&units=metric&appid={0}&cnt=24'.format(API)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT 1 FROM {ActualWeather._meta.db_table} LIMIT 1")
    except OperationalError:
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(ActualWeather)

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT 1 FROM {Forecast._meta.db_table} LIMIT 1")
    except OperationalError:
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Forecast)

    actual_response = requests.get(url)
    actual_data = actual_response.json()

    forecast_response = requests.get(forecast_url)
    forecast_raw_data = forecast_response.json()

    city_name = actual_data['name']
    temperature = actual_data['main']['temp']
    description = actual_data['weather'][0]['description']
    icon = actual_data['weather'][0]['icon']

    existing_weather_data = ActualWeather.objects.first()

    if existing_weather_data:
        existing_weather_data.city_name = city_name
        existing_weather_data.temperature = temperature
        existing_weather_data.description = description
        existing_weather_data.icon = icon
        existing_weather_data.date_time=timezone.now()
        existing_weather_data.save()
    else:
        ActualWeather.objects.create(
            city_name=city_name,
            temperature=temperature,
            description=description,
            icon=icon,
            date_time=timezone.now()
        )

    for forecast in forecast_raw_data['list']:
        date_time = timezone.datetime.utcfromtimestamp(forecast['dt'])
        existing_forecast = Forecast.objects.filter(city_name=city_name, date_time=date_time).first()

        if existing_forecast:
            existing_forecast.temperature = forecast['main']['temp']
            existing_forecast.description = forecast['weather'][0]['description']
            existing_forecast.icon = forecast['weather'][0]['icon']
            existing_forecast.date_time = date_time
            existing_forecast.save()
        else:
            Forecast.objects.create(
                city_name=city_name,
                temperature=forecast['main']['temp'],
                description=forecast['weather'][0]['description'],
                icon=forecast['weather'][0]['icon'],
                date_time=date_time
            )