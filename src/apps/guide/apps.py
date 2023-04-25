from django.apps import AppConfig


class GuideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.guide'
    verbose_name = "Справочник"
    verbose_name_plural = 'Справочники'
