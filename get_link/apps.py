from django.apps import AppConfig


class GetLinkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'get_link'

    def ready(self):
        import get_link.signals
