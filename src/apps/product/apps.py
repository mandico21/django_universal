from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.product'
    verbose_name = "продукт"
    verbose_name_plural = 'продукты'
