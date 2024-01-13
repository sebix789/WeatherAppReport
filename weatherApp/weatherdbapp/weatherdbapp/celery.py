from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weatherdbapp.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('weatherdbapp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(300.0, 'weatherfront.tasks.weather_data_fetch_and_update', name='fetch-weather-data')
    
app.conf.beat_schedule = {
    'fetch-weather-data': {
        'task': 'weatherfront.tasks.weather_data_fetch_and_update',
        'schedule': crontab(minute='*/5'),
    },
}