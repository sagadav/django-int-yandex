from django.db import models


class Feedback(models.Model):
    mail = models.EmailField(max_length=80)
    text = models.TextField()
    created_on = models.DateField()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
