from django.contrib import admin

from apps.guide.models import Warehouse, City


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    # list_display = (,)
    pass
