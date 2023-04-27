from django.db import models

from apps.common.models import TimedBaseModel


class Brand(TimedBaseModel):
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    name = models.CharField('Название')
    description = models.TextField('Описание', null=True, blank=True)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name
