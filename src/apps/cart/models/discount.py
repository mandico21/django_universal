from django.db import models

from apps.common.models import TimedBaseModel
from apps.shop.models import ProductType, CategoryNode, Product


class Discount(TimedBaseModel):
    class DiscountType(models.TextChoices):
        PR = "percent", "Процентная"
        FX = "fixed", "Фиксированная"

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    name = models.CharField('Название', max_length=64)
    description = models.CharField(
        'Описание',
        max_length=255,
        null=True,
        blank=True
    )
    discount_type = models.CharField(
        'Тип скидки',
        choices=DiscountType.choices
    )
    discount_value = models.DecimalField(
        'Значение скидки',
        max_digits=8,
        decimal_places=2
    )
    categories = models.ManyToManyField(CategoryNode)
    products = models.ManyToManyField(ProductType)
    min_order_amount = models.DecimalField(
        'Минимальная сумма для работы скидки',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    is_active = models.BooleanField('Активна', default=True)

    def __str__(self) -> str:
        return f'{self.name} {self.discount_type} {self.discount_value}'


class Coupon(TimedBaseModel):
    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    name = models.CharField('Название', max_length=64)
    description = models.CharField(
        'Описание',
        max_length=255,
        null=True,
        blank=True
    )
    code = models.CharField('Купон', max_length=64)
    discount = models.ForeignKey(
        Discount,
        verbose_name='Скидка для купона',
        on_delete=models.PROTECT
    )
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    is_active = models.BooleanField('Активна', default=True)

    def __str__(self) -> str:
        return f'{self.name} {self.code}'


class Gift(TimedBaseModel):
    class Meta:
        verbose_name = 'Подарок'
        verbose_name_plural = 'Подарки'

    name = models.CharField('Название', max_length=64)
    description = models.CharField(
        'Описание',
        max_length=255,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'{self.name} {self.product}'


class GiftCoupon(TimedBaseModel):
    class Meta:
        verbose_name = 'Купон подарка'
        verbose_name_plural = 'Купоны подарков'

    gift = models.ForeignKey(
        Gift,
        verbose_name='Подарок',
        on_delete=models.PROTECT
    )
    code = models.CharField('Купон', max_length=64)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    is_active = models.BooleanField('Активна', default=True)

    def __str__(self) -> str:
        return f'{self.gift} {self.code}'
