from django.contrib import admin

from apps.common.admin import CacheAdminMixin
from apps.imageledger.models import ImageLedger


@admin.register(ImageLedger)
class ImageLedgerAdmin(CacheAdminMixin):
    list_display = ('image', 'id')
