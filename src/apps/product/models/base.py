from django.db import models


class TimedBaseModel(models.Model):
    """Основная модель с датой"""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)