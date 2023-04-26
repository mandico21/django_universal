from django.contrib import admin

from apps.imageledger.models import ImageLedger


@admin.register(ImageLedger)
class ImageLedgerAdmin(admin.ModelAdmin):
    list_display = ('image', 'id')
