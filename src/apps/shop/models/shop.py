from django.db import models

from apps.product.models import TimedBaseModel
from apps.shop.models import City


class Shop(TimedBaseModel):
    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'

    name = models.CharField('название')
    description = models.CharField('описание', null=True, blank=True)
    city = models.ForeignKey(City, verbose_name='город', on_delete=models.CASCADE, related_name='shops')
    address = models.CharField('адрес магазина')
    phone = models.CharField('номер телефона', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.phone}'
