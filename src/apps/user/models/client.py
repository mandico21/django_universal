import uuid

from django.db import models

from apps.shop.models import TimedBaseModel


class Client(TimedBaseModel):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    uuid = models.UUIDField('ID клиента', default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField('Имя', max_length=64, blank=True, null=True)
    middle_name = models.CharField('Отчество', max_length=64, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=64, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=64, blank=True, null=True)
    email = models.CharField('Email', max_length=120, blank=True, null=True)

    @property
    def full_name(self) -> str:
        if self.middle_name:
            return f'{self.first_name} {self.middle_name} {self.last_name}'
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'Client {self.uuid}'
