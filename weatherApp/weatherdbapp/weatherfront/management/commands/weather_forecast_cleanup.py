from django.core.management.base import BaseCommand
from weatherfront.models import Forecast

class Command(BaseCommand):
    help = 'Clean up forecast data in the database'

    def handle(self, *args, **options):
        self.stdout.write("Cleaning up forecast data...")
        Forecast.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Forecast data cleaned up successfully."))
