from django.contrib import admin

from apps.common.admin import CacheAdminMixin
from .models import Review, Favorite, Client


@admin.register(Client)
class ClientAdmin(CacheAdminMixin):
    list_display = ('uuid', 'first_name', 'last_name', 'phone')


@admin.register(Review)
class ReviewAdmin(CacheAdminMixin):
    list_display = ('client', 'product', 'comment', 'rating',)


@admin.register(Favorite)
class FavoriteAdmin(CacheAdminMixin):
    list_display = ('client', 'product',)
