from django.apps import AppConfig


class CitaConfig(AppConfig):
    name = 'cita'

    def ready(self):
        from . import updater
        updater.start()