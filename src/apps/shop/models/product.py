from django.db import models

from apps.guide.models import Warehouse
from apps.guide.models.brand import Brand
from apps.imageledger.models import ImageLedger
from apps.shop.models import TimedBaseModel
from apps.shop.services.discount_percentage import DiscountPercentage


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
    images = models.ManyToManyField(ImageLedger, blank=True, related_name='product_images')
    poster = models.ImageField('Постер', upload_to='product/poster')
    name = models.CharField('Название', max_length=60)
    description = models.TextField('Описание', null=True, blank=True)
    base_price = models.DecimalField('Базовая цена', max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField('Цена со скидкой', max_digits=10, decimal_places=2)

    @property
    def discount(self) -> int | None:
        return DiscountPercentage()(self.price, self.base_price)

    discount.fget.short_description = 'Скидка'

    @property
    def img_path(self) -> str:
        return f'django_universal/src/{self.poster}'

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
    warehouse = models.ForeignKey(Warehouse,
                                  verbose_name='Магазин',
                                  on_delete=models.CASCADE,
                                  related_name='products')
    quantity = models.IntegerField('Количество', default=0)

    def __str__(self) -> str:
        return f'{self.product} - {self.warehouse}'


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
