from django.apps import AppConfig


class BrandsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.brands'
    verbose_name = "Бренд"
    verbose_name_plural = 'Бренды'
