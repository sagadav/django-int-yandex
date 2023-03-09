from catalog.validators import validate_text
import core
from django.db import models
from tinymce.models import HTMLField


class Tag(core.models.BaseSlug):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class CategoryManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .prefetch_related(
                models.Prefetch(
                    "catalog_items",
                    queryset=Item.objects.filter(is_published=True).only(
                        "name", "text", "category_id"
                    ),
                )
            )
            .prefetch_related(
                models.Prefetch(
                    "catalog_items__tags",
                    queryset=Tag.objects.filter(is_published=True).only(
                        "name"
                    ),
                )
            )
            .filter(is_published=True)
            .only("name")
            .order_by("name")
        )


class Category(core.models.BaseSlug):
    objects = CategoryManager()

    weight = models.PositiveSmallIntegerField(default=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class ImageModel(core.models.BaseImage):
    item = models.ForeignKey(
        "item",
        related_name="item_image",
        on_delete=models.CASCADE,
    )


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True, category__is_published=True)
            .select_related("category")
            .prefetch_related(
                models.Prefetch(
                    "tags",
                    queryset=Tag.objects.filter(is_published=True).only(
                        "name"
                    ),
                )
            )
            .order_by("name")
            .only("name", "text", "category__name")
        )

    def published_order_by_category(self):
        return self.published().order_by("category__name")


class Item(core.models.Base, core.models.BaseImage):
    objects = ItemManager()

    is_on_main = models.BooleanField(default=False)
    text = HTMLField(
        verbose_name="Описание",
        validators=[validate_text],
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
