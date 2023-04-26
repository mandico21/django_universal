from django.db import models

from apps.shop.models import TimedBaseModel
from apps.guide.models import City


class Warehouse(TimedBaseModel):
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE, related_name='shops')
    name = models.CharField('Название')
    description = models.CharField('Описание', null=True, blank=True)
    address = models.CharField('Адрес магазина')
    phone = models.CharField('Номер телефона', null=True, blank=True)
    email = models.CharField('Email', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.address}'
