from django.contrib import admin

from apps.shop.models import Shop, City


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    # list_display = (,)
    pass
