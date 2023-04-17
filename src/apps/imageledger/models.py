from django.db import models

from apps.product.models import TimedBaseModel


class ImageLedger(TimedBaseModel):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    image = models.ImageField('Изображение', upload_to='product')

    def __str__(self) -> str:
        return f'{self.id}'
