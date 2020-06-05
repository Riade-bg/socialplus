from django.apps import AppConfig


class ImessageConfig(AppConfig):
    name = 'imessage'
    
    def ready(self):
        from . import signals
