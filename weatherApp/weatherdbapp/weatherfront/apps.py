from django.apps import AppConfig


class WeatherfrontConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weatherfront'
    
    def ready(self):
        import weatherfront.signals
