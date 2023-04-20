from django.contrib import admin

from apps.clients.models.cart import Cart
from apps.clients.models.client import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'first_name', 'last_name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('client',)
