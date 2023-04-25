from django.db import models

from apps.shop.models import TimedBaseModel


class City(TimedBaseModel):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    name = models.CharField('Название')
    code = models.CharField('Код города')

    def __str__(self) -> str:
        return f'{self.name} - {self.code}'
