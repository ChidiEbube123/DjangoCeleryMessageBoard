from django.apps import AppConfig


class AMessageboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_messageboard'
''' def ready(self):
        import a_messageboard.signals'''