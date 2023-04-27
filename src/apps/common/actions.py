from django.contrib import messages
from django.core.cache import cache
from django.http import HttpResponseRedirect, HttpRequest

from apps.shop.management.commands.autoload import load_category


def clear_cache(request: HttpRequest) -> HttpResponseRedirect:
    cache.clear()
    messages.info(request, 'Кеш успешно сброшен')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def load_categories(request: HttpRequest) -> HttpResponseRedirect:
    counter_created, counter_updated = load_category()
    messages.info(request, f'Категории успешно импортированы. Обновлено {counter_updated} Создано {counter_created}')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
