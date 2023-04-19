from django.db import models

from apps.brands.models import Brand
from apps.imageledger.models import ImageLedger
from apps.product.models import TimedBaseModel
from apps.product.services.discount_percentage import DiscountPercentage
from apps.shop.models import Shop


class ProductType(TimedBaseModel):
    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'

    article = models.IntegerField('Артикул товара', primary_key=True)
    category = models.ForeignKey('CategoryNode',
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE,
                                 related_name='product_types')
    brand = models.ForeignKey(Brand,
                              verbose_name='Бренд',
                              on_delete=models.CASCADE,
                              null=True, blank=True,
                              related_name='product_types')
    images = models.ManyToManyField(ImageLedger, null=True, blank=True)
    name = models.CharField('Название', max_length=60)
    description = models.TextField('Описание', null=True, blank=True)
    base_price = models.DecimalField('Базовая цена', max_digits=10, decimal_places=2)
    price = models.DecimalField('Цена со скидкой', max_digits=10, decimal_places=2, null=True, blank=True)

    @property
    def discount(self) -> int | None:
        return DiscountPercentage()(self.price, self.base_price)

    discount.fget.short_description = 'Скидка'

    def __str__(self) -> str:
        return f'{self.article} - {self.name}'


class Product(TimedBaseModel):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    product = models.ForeignKey('ProductType',
                                verbose_name='Тип товара',
                                on_delete=models.CASCADE,
                                related_name='products')
    shop = models.ForeignKey(Shop,
                             verbose_name='Магазин',
                             on_delete=models.CASCADE,
                             related_name='products')
    quantity = models.IntegerField('Количество', default=0)

    def __str__(self) -> str:
        return f'{self.product} - {self.shop}'


class Attribute(TimedBaseModel):
    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(max_length=110)

    def __str__(self) -> str:
        return self.name


class AttributeValue(TimedBaseModel):
    class Meta:
        verbose_name = 'Значение атрибута'
        verbose_name_plural = 'Значение атрибутов'

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=64, null=True, blank=True)
    slug = models.SlugField(max_length=50)

    def __str__(self) -> str:
        return self.name


class ProductAttribute(TimedBaseModel):
    class Meta:
        verbose_name = 'Атрибуты товара'
        verbose_name_plural = 'Атрибуты товаров'

    product = models.ForeignKey(ProductType,
                                verbose_name='Товар',
                                on_delete=models.CASCADE,
                                related_name='attributes')
    attribute = models.ForeignKey(Attribute,
                                  verbose_name='Аттрибуты',
                                  on_delete=models.CASCADE,
                                  related_name='products')
    meaning = models.CharField('Значение', max_length=64)
    value = models.ForeignKey(AttributeValue,
                              verbose_name='Величина',
                              null=True, blank=True,
                              on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product} - {self.attribute} - {self.meaning} - {self.value}'
