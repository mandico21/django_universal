from django.db import models

from apps.shop.models import TimedBaseModel


class ImageLedger(TimedBaseModel):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    image = models.ImageField('Изображение', upload_to='product')

    @property
    def url_path(self) -> str:
        return f'django_universal/src/media/{self.image}'

    def __str__(self) -> str:
        return f'{self.id} - {self.image}'
