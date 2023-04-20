from django.db import models

from apps.clients.models.client import Client
from apps.product.models import TimedBaseModel, Product


class Cart(TimedBaseModel):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    client = models.ForeignKey(Client,
                               verbose_name='Клиент',
                               on_delete=models.CASCADE,
                               related_name='carts')

    def __str__(self) -> str:
        return f'Cart ({self.client_id})'


class Item(TimedBaseModel):
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    cart = models.ForeignKey(Cart,
                             verbose_name='Корзина',
                             on_delete=models.CASCADE,
                             related_name='items')
    product = models.ForeignKey(Product,
                                verbose_name='Товар',
                                on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество', default=0)

    def __str__(self) -> str:
        return f'Item ({self.cart_id} - {self.product_id})'
