from django.db import models

from apps.shop.models import TimedBaseModel, ProductType
from apps.user.models import Client


class Favorite(TimedBaseModel):
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    client = models.ForeignKey(Client, verbose_name='Покупатель', on_delete=models.CASCADE)
    product = models.ForeignKey(ProductType, verbose_name='Товар', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.client} {self.product}'
