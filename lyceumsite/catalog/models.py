from catalog.validators import validate_text
import core
from django.db import models
from django.utils.html import mark_safe
from sorl.thumbnail import get_thumbnail


class Tag(core.models.BaseSlug):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(core.models.BaseSlug):
    weight = models.PositiveSmallIntegerField(default=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class ImageModel(models.Model):
    image = models.ImageField("Изображение", upload_to="catalog/")
    item = models.ForeignKey(
        "item",
        on_delete=models.CASCADE,
    )

    def get_image_x1280(self):
        return get_thumbnail(self.image, "1280", quality=51)

    def get_image_300x300(self):
        return get_thumbnail(self.image, "300x300", quality=51, crop="center")

    def image_tbh(self):
        if self.image:
            return mark_safe(f"<img src='{self.get_image_300x300().url}' />")
        else:
            return "Изображения нет"

    list_display = ("image_tbh",)
    readonly_fields = ("image_tbh",)


class Item(core.models.Base):
    main_image = models.ImageField(
        "Главное изображение",
        upload_to="catalog/",
        null=True,
        blank=True,
    )
    text = models.TextField(
        verbose_name="Описание", validators=[validate_text]
    )
    category = models.ForeignKey(
        "category",
        verbose_name="Категория",
        related_name="catalog_items",
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")

    def get_image_300x300(self):
        return get_thumbnail(
            self.main_image, "300x300", quality=51, crop="center"
        )

    def image_tbh(self):
        if self.main_image:
            return mark_safe(f"<img src='{self.get_image_300x300().url}' />")
        else:
            return "Изображения нет"

    image_tbh.short_description = "Главное изображение"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
