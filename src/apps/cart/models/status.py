from django.db import models


class Status(models.TextChoices):
    NEW = "new", "Новая"
    ACT = "active", "Активная"
    ORD = "ordered", "Оформленная"
    CLD = "cancelled", "Отмененная"
    RFD = "refunded", "Возврат"
    CMD = "completed", "Завершенная"
