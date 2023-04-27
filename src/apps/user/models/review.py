from django.db import models

from apps.common.models import TimedBaseModel
from apps.shop.models import ProductType
from .client import Client


class Review(TimedBaseModel):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    product = models.ForeignKey(
        ProductType,
        verbose_name='Товар',
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    client = models.ForeignKey(
        Client,
        verbose_name='Клиент',
        on_delete=models.PROTECT
    )
    dignity = models.CharField('Достоинство', max_length=225)
    shortcomings = models.CharField('Недостатки', max_length=225)
    comment = models.CharField('Комментарий', max_length=525)
    rating = models.IntegerField('Рейтинг')

    def __str__(self) -> str:
        return f'{self.product} - {self.client}'
