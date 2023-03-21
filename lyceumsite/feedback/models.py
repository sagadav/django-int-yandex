from django.db import models


class Feedback(models.Model):
    class Status(models.TextChoices):
        RECEIVED = "received", "Получено"
        PENDING = "pending", "В обработке"
        ANSWERED = "answered", "Ответ дан"

    mail = models.EmailField(max_length=80)
    text = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.RECEIVED,
    )
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return self.mail
