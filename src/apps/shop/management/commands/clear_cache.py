from django.core.cache import cache
from django.core.management import BaseCommand

from apps.common.actions import clear_cache


class Command(BaseCommand):

    def handle(self, *args, **options):
        cache.clear()
