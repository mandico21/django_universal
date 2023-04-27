from django.contrib import admin
from django.urls import path

from apps.common.actions import clear_cache, load_categories
from apps.shop.management.commands.autoload import load_category


class BaseModelAdmin(admin.ModelAdmin):
    # Общие настройки для всех моделей
    list_per_page = 50
    readonly_fields = ('created_at', 'updated_at')


class CategoryAdminMixin(BaseModelAdmin):
    change_list_template = 'admin/button_import_category.html'

    def get_urls(self):
        urls = super().get_urls()
        shard_urls = [
            path(r'clear_cache', clear_cache, name='clear_cache'),
            path(r'load_category', load_categories, name='load_category'),
        ]
        return shard_urls + urls


class CacheAdminMixin(BaseModelAdmin):
    change_list_template = 'admin/button_import_cache.html'

    def get_urls(self):
        urls = super().get_urls()
        shard_urls = [
            path(r'clear_cache', clear_cache, name='clear_cache'),
        ]
        return shard_urls + urls
