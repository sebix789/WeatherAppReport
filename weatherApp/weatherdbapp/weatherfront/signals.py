from django.core.signals import request_started
from django.dispatch import receiver
from django.core.management import call_command

# TODO: maybe later
# @receiver(request_started)
# def cleanup_forecast(sender, **kwargs):
#     call_command('weather_forecast_cleanup')