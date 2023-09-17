from django.apps import AppConfig


class ShipmentConfig(AppConfig):
    name = 'shipment'
from django.apps import AppConfig

class signals(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shipment'

    def ready(self):
        import shipment.signals  # Import the signals module
