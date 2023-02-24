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
    slug = models.SlugField(
        verbose_name="Артикул",
        unique=True,
        max_length=200,
    )

    class Meta:
        abstract = True
