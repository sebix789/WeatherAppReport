from django.views import View
from django.shortcuts import render
from .models import ActualWeather, Forecast


class WeatherView(View):
    template_name = 'weather.html'
    
    def get(self, request, *args, **kwargs):
        if ActualWeather.objects.exists() or Forecast.objects.exists():
            city_data = ActualWeather.objects.first()
            if city_data:
                weather_data = ActualWeather.objects.filter(city_name=city_data.city_name).first()
                forecast_data = Forecast.objects.filter(city_name=city_data.city_name).order_by('date_time')[:3]
        
                context = {
                    'city_name': weather_data.city_name,
                    'temperature': weather_data.temperature,
                    'description': weather_data.description,
                    'icon': weather_data.icon,
                    'forecast_data': forecast_data,
                }

                return render(request, self.template_name, context)
        
        return render(request, self.template_name)
            
