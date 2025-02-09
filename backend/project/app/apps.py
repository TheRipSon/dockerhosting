from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.app'  # Use the full path to the app

    def ready(self):
        import project.app.signals  # noqa: F401

