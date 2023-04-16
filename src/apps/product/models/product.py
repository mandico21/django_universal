from _decimal import Decimal
from django.db import models

from apps.product.models import TimedBaseModel
from apps.shop.models import Shop


class ProductType(TimedBaseModel):
    class Meta:
        verbose_name = 'тип товара'
        verbose_name_plural = 'типы товаров'

    article = models.IntegerField('артикул товара', primary_key=True)
    category = models.ForeignKey('CategoryNode',
                                 verbose_name='категория',
                                 on_delete=models.CASCADE,
                                 related_name='product_types')
    name = models.CharField('название', max_length=60)
    description = models.TextField('описание', null=True, blank=True)
    base_price = models.DecimalField('базовая цена', max_digits=10, decimal_places=2)
    price = models.DecimalField('цена со скидкой', max_digits=10, decimal_places=2, null=True, blank=True)

    @property
    def discount(self) -> Decimal:
        if self.base_price and self.price:
            return (self.price / self.base_price) * 100

    discount.fget.short_description = 'Скидка'

    def __str__(self) -> str:
        return f'{self.article} - {self.name}'


class Product(TimedBaseModel):
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    product = models.ForeignKey('ProductType',
                                verbose_name='тип товара',
                                on_delete=models.CASCADE,
                                related_name='products')
    shop = models.ForeignKey(Shop,
                             verbose_name='магазин',
                             on_delete=models.CASCADE,
                             related_name='products')
    quantity = models.IntegerField('количество', default=0)

    def __str__(self) -> str:
        return f'{self.product} - {self.shop}'
