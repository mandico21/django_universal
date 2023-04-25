from django.contrib import admin

from apps.user.models import Review
from apps.user.models.client import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'first_name', 'last_name',)



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name',)
