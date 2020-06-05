from django.apps import AppConfig


class WeshareConfig(AppConfig):
    name = 'social'

    def ready(self):
        from . import signals
