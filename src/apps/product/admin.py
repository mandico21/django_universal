from django.contrib import admin

from apps.product.models import Category, CategoryNode, ProductType, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)


@admin.register(CategoryNode)
class CategoryNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'parent_id',)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('article', 'discount')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'shop', 'quantity',)
