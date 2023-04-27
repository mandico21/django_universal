from django.core.management import BaseCommand

from apps.common.actions import clear_cache


class Command(BaseCommand):

    def handle(self, *args, **options):
        clear_cache()
