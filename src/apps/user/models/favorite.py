from django.db import models

from apps.common.models import TimedBaseModel
from apps.shop.models import ProductType
from apps.user.models import Client


class Favorite(TimedBaseModel):
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    client = models.ForeignKey(
        Client,
        verbose_name='Покупатель',
        on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        ProductType,
        verbose_name='Товар',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'{self.client} {self.product}'
