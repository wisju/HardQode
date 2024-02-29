from django.apps import AppConfig


class EducationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "education_api"

    def ready(self):
        """Сигнал, который запускается при сохранении объекта UserProductAccess"""
        import education_api.signals
