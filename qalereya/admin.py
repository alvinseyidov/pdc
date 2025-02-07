from django.contrib import admin
from django.utils.html import mark_safe
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    search_fields = ['id']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="75" height="75" style="object-fit: cover; border-radius: 5px;" />')
        return "-"

    image_preview.short_description = "Şəkil Önizləmə"
