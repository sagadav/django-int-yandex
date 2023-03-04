import catalog.models
from django.contrib import admin


class GalleryInline(admin.StackedInline):
    list_display = "image_tbh"
    model = catalog.models.ImageModel


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
        "image_tbh",
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)
    inlines = [GalleryInline]


admin.site.register(catalog.models.Category)
admin.site.register(catalog.models.Tag)
