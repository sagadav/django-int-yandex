from django.core.exceptions import ValidationError
from django.db import models


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
