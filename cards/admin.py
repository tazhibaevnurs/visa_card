from django.contrib import admin
from .models import CardApplication


@admin.register(CardApplication)
class CardApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'telegram_username', 'phone', 'source', 'created_at')
    list_filter = ('source', 'created_at')
    search_fields = ('name', 'phone', 'telegram_username', 'comment')
    readonly_fields = ('created_at',)
