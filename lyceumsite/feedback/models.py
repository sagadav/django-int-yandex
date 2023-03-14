from django.db import models


class Feedback(models.Model):
    mail = models.EmailField(max_length=80)
    text = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
