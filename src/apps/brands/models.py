from django.db import models

from apps.product.models import TimedBaseModel


class Brand(TimedBaseModel):
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    name = models.CharField('Название')
    description = models.TextField('Описание', null=True, blank=True)

    # img

    def __str__(self) -> str:
        return self.name
