from core.validators import validate_slug
from django.db import models


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
    slug = models.TextField(
        verbose_name="Артикул",
        unique=True,
        max_length=200,
        validators=[validate_slug],
    )

    class Meta:
        abstract = True
