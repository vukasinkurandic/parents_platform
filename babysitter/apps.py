from django.apps import AppConfig


class BabysitterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'babysitter'

    def ready(self):
        import babysitter.signals
