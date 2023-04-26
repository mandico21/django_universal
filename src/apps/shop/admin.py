from django.contrib import admin
from django.core.files import images

from apps.shop.models import Category, CategoryNode, ProductType, Product, Attribute, ProductAttribute, \
    AttributeValue
from apps.user.models import Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    list_display_links = ('id', 'name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CategoryNode)
class CategoryNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'parent_id',)
    list_display_links = ('id', 'category',)


class AttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 0
    classes = ['collapse']
    verbose_name = 'Атрибуты'
    verbose_name_plural= 'Атрибуты'


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    classes = ['collapse']



class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    classes = ['collapse']



@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'category', 'brand', 'price')
    list_display_links = ('article', 'name', 'category',)
    filter_horizontal = ('images',)
    list_filter = ('category', 'brand',)
    inlines = [AttributeInline, ReviewInline, ProductInline]
    save_on_top = True
    fieldsets = [
        (None, {
            'fields': (('article', 'category', 'brand',),)
        }),
        (None, {
            'fields': ('name', 'description')
        }),
        (None, {
            'fields': (('price', 'base_price', 'discount'),)
        }),
        (None, {
            'fields': ('poster', 'images'),
        }),
        (None, {
            'fields': (('created_at', 'updated_at'),)
        })
    ]
    readonly_fields = ('discount', 'created_at', 'updated_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'quantity',)
    list_display_links = ('product', 'warehouse',)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('product', 'attribute', 'value')
