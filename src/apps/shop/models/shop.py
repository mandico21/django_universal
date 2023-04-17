from django.db import models

from apps.product.models import TimedBaseModel
from apps.shop.models import City


class Shop(TimedBaseModel):
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    name = models.CharField('Название')
    description = models.CharField('Описание', null=True, blank=True)
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE, related_name='shops')
    address = models.CharField('Адрес магазина')
    phone = models.CharField('Номер телефона', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.phone}'
