from django.contrib import admin
from .models import Yenilikler

@admin.register(Yenilikler)
class YeniliklerAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'author']
    list_filter = ['created_at']
