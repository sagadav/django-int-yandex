from catalog.validators import validate_text
import core
from django.db import models
<<<<<<< HEAD
=======
from tinymce.models import HTMLField
>>>>>>> 3752c1b76be3395f4d8d09cd0fd245951c9ada97


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
        related_name="item_image",
        on_delete=models.CASCADE,
    )


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .select_related("category")
            .prefetch_related(
                models.Prefetch(
                    "tags", queryset=Tag.objects.all().only("name")
                )
            )
            .only("name", "text", "category__name")
        )


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
