from django.contrib import admin

from .models import Review, Favorite, Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'first_name', 'last_name', 'phone')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('client', 'product', 'comment', 'rating',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('client', 'product',)
