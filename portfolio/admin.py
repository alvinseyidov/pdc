from django.contrib import admin
from .models import Category, Project, Images


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1  # Allows adding extra images inline
    fields = ['images']
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.images:
            return f'<img src="{obj.images.url}" width="100" height="100" style="object-fit: cover;" />'
        return "-"

    preview.allow_tags = True
    preview.short_description = "Image Preview"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_categories']
    list_filter = ['category']
    search_fields = ['name']
    inlines = [ImagesInline]

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    display_categories.short_description = "Categories"



