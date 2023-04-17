from django.contrib import admin

from apps.product.models import Category, CategoryNode, ProductType, Product, Attribute, ProductAttribute, \
    AttributeValue


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


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug',)


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('product', 'attribute', 'value')
