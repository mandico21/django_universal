from django.contrib import admin

from apps.product.models import Category, CategoryNode


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)


@admin.register(CategoryNode)
class CategoryNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'parent_id',)
