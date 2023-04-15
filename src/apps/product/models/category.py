from django.db import models

from apps.product.models import TimedBaseModel


class Category(TimedBaseModel):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    id = models.IntegerField('id категории', primary_key=True)
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

    id = models.IntegerField('id подкатегории', primary_key=True)
    category = models.ForeignKey('Category', verbose_name='категория', on_delete=models.CASCADE)
    # parent_id = models.IntegerField('родитель', null=True, blank=True)
    parent = models.ForeignKey('self', verbose_name='категория', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __repr__(self) -> str:
        return f'CategoryNode ({self.id})'

    def __str__(self) -> str:
        return f'{self.id} - {self.category.name}'
