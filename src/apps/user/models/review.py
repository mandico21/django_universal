from django.db import models

from apps.shop.models import TimedBaseModel, ProductType


class Review(TimedBaseModel):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    product = models.ForeignKey(ProductType,
                                verbose_name='Товар',
                                on_delete=models.CASCADE,
                                related_name='reviews')
    name = models.CharField('ФИО', max_length=120)
    phone = models.CharField('Номер телефона', max_length=20)
    dignity = models.CharField('Достоинство', max_length=225)
    shortcomings = models.CharField('Недостатки', max_length=225)
    comment = models.CharField('Комментарий', max_length=525)
    rating = models.IntegerField('Рейтинг')

    def __str__(self) -> str:
        return f'{self.product} - {self.name}'
