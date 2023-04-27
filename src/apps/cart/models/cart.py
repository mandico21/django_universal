from django.db import models
from django.db.models import Sum, F

from apps.common.models import TimedBaseModel
from apps.shop.models import Product
from apps.user.models.client import Client
from .status import Status


class Cart(TimedBaseModel):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.PROTECT, related_name='carts')
    status = models.CharField('Статус', choices=Status.choices, default=Status.NEW)

    def __str__(self) -> str:
        return f'Корзина ({self.client_id})'

    @property
    def total_amount(self) -> int:
        # i = int()
        # for item in self.items.all():
        #     i += item.product.product.price
        return self.items.aggregate(total_amount=Sum(F('product__product__price') * F('quantity')))['total_amount']

    total_amount.fget.short_description = 'Общая сумма'


class CartItem(TimedBaseModel):
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
        unique_together = ('cart', 'product',)

    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.PROTECT)
    quantity = models.IntegerField('Количество', default=0)

    def __str__(self) -> str:
        return f'{self.cart} / {self.product_id}'
