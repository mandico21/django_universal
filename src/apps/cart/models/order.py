from django.db import models

from apps.common.models import TimedBaseModel
from apps.shop.models import Product
from .cart import Cart
from .discount import Discount, Coupon, GiftCoupon
from .status import Status


class Order(TimedBaseModel):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.PROTECT)
    status = models.CharField('Статус', choices=Status.choices, default=Status.NEW)
    discount = models.ForeignKey(Discount, verbose_name='Скидка', on_delete=models.PROTECT)
    coupon = models.ForeignKey(Coupon, verbose_name='Купон', on_delete=models.PROTECT)
    gift_coupon = models.ForeignKey(GiftCoupon, verbose_name='Купон подарка', on_delete=models.PROTECT)
    total_amount = models.IntegerField('Итоговая сумма')
    amount = models.IntegerField('Сумма скидки')

    def __str__(self) -> str:
        return f'{self.cart} - {self.status} - {self.total_amount}'


class OrderDetail(TimedBaseModel):
    class Meta:
        verbose_name = 'Деталь заказа'
        verbose_name_plural = 'Детали заказа'

    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.PROTECT)
    price = models.IntegerField('Цена')
    quantity = models.IntegerField('Количество')

    def __str__(self) -> str:
        return f'{self.order} -{self.product}'
