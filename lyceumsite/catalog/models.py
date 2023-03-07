from catalog.validators import validate_text
import core
from django.db import models


class Tag(core.models.BaseSlug):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(core.models.BaseSlug):
    weight = models.PositiveSmallIntegerField(default=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class ImageModel(core.models.BaseImage):
    item = models.ForeignKey(
        "item",
        on_delete=models.CASCADE,
    )


class Item(core.models.Base, core.models.BaseImage):
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

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
