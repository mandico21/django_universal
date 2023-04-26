from django.contrib import admin

from apps.guide.models import Warehouse, City
from apps.shop.models import ProductType, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    classes = ['collapse']


class WarehouseInline(admin.TabularInline):
    model = Warehouse
    extra = 0
    classes = ['collapse']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'description', 'address',)
    list_display_links = ('name', 'city',)
    inlines = [ProductInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)
    list_display_links = ('name', 'code',)
    inlines = [WarehouseInline]
