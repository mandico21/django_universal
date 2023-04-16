from django.db import models

from apps.product.models import TimedBaseModel


class City(TimedBaseModel):
    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    name = models.CharField('название')
    code = models.CharField('код города')

    def __str__(self) -> str:
        return f'{self.name} - {self.code}'
