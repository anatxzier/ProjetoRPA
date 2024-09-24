from django.apps import AppConfig


class GeenfyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geenfy'
    
    def ready(self):
        import geenfy.signals  