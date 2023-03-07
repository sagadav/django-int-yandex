from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import mark_safe
from sorl.thumbnail import get_thumbnail


from .utils import normalize_name


class Base(models.Model):
    is_published = models.BooleanField(
        verbose_name="Опубликован", help_text="Да/Нет", default=True
    )
    name = models.CharField(verbose_name="Название", max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name[:20]


class BaseSlug(Base):
    slug = models.SlugField(
        verbose_name="Артикул",
        unique=True,
        max_length=200,
    )
    normalized_name = models.CharField(
        editable=False,
        default="",
        verbose_name="Нормализированное название",
        max_length=150,
    )

    class Meta:
        abstract = True

    def clean(self):
        count = (
            self.__class__.objects.filter(
                normalized_name=normalize_name(self.name)
            )
            .exclude(pk=self.pk)
            .count()
        )
        if count > 0:
            raise ValidationError({"name": ["Такое название уже есть"]})

    def save(self, *args, **kwargs):
        self.normalized_name = normalize_name(self.name)
        return super().save(*args, **kwargs)


class BaseImage(models.Model):
    image = models.ImageField("Изображение", upload_to="img/", blank=True)

    class Meta:
        abstract = True

    def get_image_x1280(self):
        return get_thumbnail(self.image, "1280", quality=51)

    def get_image_300x300(self):
        return get_thumbnail(self.image, "300x300", quality=51, crop="center")

    def image_tbh(self):
        if self.image:
            return mark_safe(f"<img src='{self.get_image_300x300().url}' />")
        else:
            return "Изображения нет"

    image_tbh.short_description = "Изображение"
