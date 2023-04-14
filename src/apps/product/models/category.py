from django.db import models

from apps.product.models import TimedBaseModel


class Category(TimedBaseModel):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField('название', max_length=64)
    description = models.CharField('описание', max_length=120, null=True, blank=True)

    def __repr__(self) -> str:
        return f'Category ({self.name})'

    def __str__(self) -> str:
        return f'{self.name}'


class CategoryNode(TimedBaseModel):
    class Meta:
        verbose_name = 'подкатегоря'
        verbose_name_plural = 'подкатегории'

    category = models.ForeignKey('Category', verbose_name='категория', on_delete=models.CASCADE)
    parent_id = models.IntegerField('родитель', null=True, blank=True)

    def __repr__(self) -> str:
        return f'CategoryNode ({self.id})'

    def __str__(self) -> str:
        return f'{self.id}'
