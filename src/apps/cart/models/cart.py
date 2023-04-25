from django.db import models

from apps.shop.models import TimedBaseModel, Product
from apps.user.models.client import Client


class Cart(TimedBaseModel):
    class Status(models.TextChoices):
        NEW = "new", "Новая"
        ACT = "active", "Активная"
        ORD = "ordered", "Оформленная"
        CLD = "cancelled", "Отмененная"
        RFD = "refunded", "Возврат"
        CMD = "completed", "Завершенная"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE, related_name='carts')
    status = models.CharField('Статус', choices=Status.choices, default=Status.NEW)

    def __str__(self) -> str:
        return f'Cart ({self.client_id})'


class CartItem(TimedBaseModel):
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество', default=0)

    def __str__(self) -> str:
        return f'Item ({self.cart_id} - {self.product_id})'
