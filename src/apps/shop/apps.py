from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.shop'
    verbose_name = "Магазин"
    verbose_name_plural = 'Магазины'

    def ready(self):
        import apps.shop.signals
