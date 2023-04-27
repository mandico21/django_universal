from django.db import models

from apps.common.models import TimedBaseModel


class Category(TimedBaseModel):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    id = models.IntegerField('ID категории', primary_key=True)
    name = models.CharField('Название', max_length=64)
    description = models.CharField(
        'Описание',
        max_length=120,
        null=True,
        blank=True
    )
    slug = models.SlugField(max_length=80)

    def __str__(self) -> str:
        return f'{self.name}'


class CategoryNode(TimedBaseModel):
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    id = models.IntegerField('ID подкатегории', primary_key=True)
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        on_delete=models.PROTECT,
        related_name='category_nodes'
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='ID подкатегории',
        on_delete=models.PROTECT,
        null=True, blank=True,
        related_name='childrens'
    )

    def __str__(self) -> str:
        return f'{self.id} - {self.category.name}'
