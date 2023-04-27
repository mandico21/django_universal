from django.contrib import admin

from apps.common.admin import CategoryAdminMixin, CacheAdminMixin
from apps.shop.models import Category, CategoryNode, ProductType, Product, \
    Attribute, ProductAttribute, AttributeValue
from apps.user.models import Review


@admin.register(Category)
class CategoryAdmin(CategoryAdminMixin):
    list_display = ('id', 'name', 'description',)
    list_display_links = ('id', 'name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CategoryNode)
class CategoryNodeAdmin(CategoryAdminMixin):
    list_display = ('id', 'category', 'parent_id',)
    list_display_links = ('id', 'category',)


class AttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 0
    classes = ['collapse']
    verbose_name = 'Атрибуты'
    verbose_name_plural = 'Атрибуты'


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    classes = ['collapse']


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    classes = ['collapse']


@admin.register(ProductType)
class ProductTypeAdmin(CacheAdminMixin):
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
    # Выводит принудительно поля
    readonly_fields = ('discount', 'created_at', 'updated_at')
    # Добавляет фильтр по дате
    date_hierarchy = 'created_at'
    # Заменяет - т.е. полу пустое, на заданный текст
    empty_value_display = 'отсутствует'
    # select_related
    list_select_related = True
    # Меняем обычный select на новый
    # autocomplete_fields = ('category',)


@admin.register(Product)
class ProductAdmin(CacheAdminMixin):
    list_display = ('product', 'warehouse', 'quantity',)
    list_display_links = ('product', 'warehouse',)


@admin.register(Attribute)
class AttributeAdmin(CacheAdminMixin):
    list_display = ('name', 'description', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(AttributeValue)
class AttributeValueAdmin(CacheAdminMixin):
    list_display = ('name', 'description', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductAttribute)
class ProductAttributeAdmin(CacheAdminMixin):
    list_display = ('product', 'attribute', 'value')
