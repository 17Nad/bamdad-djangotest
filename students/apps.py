from django.apps import AppConfig
# from . import signals


class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
    
    def ready(self):
        from . import signals
