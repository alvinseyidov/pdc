from django.contrib import admin
from django.utils.html import mark_safe
from .models import Xidmetler, XidmetlerAltKateqoriya, Images


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1  # Allows adding extra images inline
    fields = ['images', 'preview']
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.images:
            return mark_safe(f'<img src="{obj.images.url}" width="100" height="100" style="object-fit: cover;" />')
        return "-"

    preview.short_description = "Şəkil önizləmə"


@admin.register(Xidmetler)
class XidmetlerAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon_preview', 'image_preview']
    search_fields = ['name']
    inlines = [ImagesInline]

    def icon_preview(self, obj):
        if obj.iconimage:
            return mark_safe(f'<img src="{obj.iconimage.url}" width="50" height="50" style="object-fit: cover;" />')
        return "-"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;" />')
        return "-"

    icon_preview.short_description = "İkon önizləmə"
    image_preview.short_description = "Şəkil önizləmə"


@admin.register(XidmetlerAltKateqoriya)
class XidmetlerAltKateqoriyaAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'icon_preview', 'image_preview']
    search_fields = ['name', 'category__name']

    def icon_preview(self, obj):
        if obj.iconimage:
            return mark_safe(f'<img src="{obj.iconimage.url}" width="50" height="50" style="object-fit: cover;" />')
        return "-"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;" />')
        return "-"

    icon_preview.short_description = "İkon önizləmə"
    image_preview.short_description = "Şəkil önizləmə"


