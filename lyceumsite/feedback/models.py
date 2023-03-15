from django.db import models


class Feedback(models.Model):
    mail = models.EmailField(max_length=80)
    text = models.TextField()
    RECEIVED = "received"
    PENDING = "pending"
    ANSWERED = "answered"
    status = models.CharField(
        max_length=20,
        choices=[
            (RECEIVED, "получено"),
            (PENDING, "в обработке"),
            (ANSWERED, "ответ дан"),
        ],
        default=PENDING,
    )
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return self.mail
