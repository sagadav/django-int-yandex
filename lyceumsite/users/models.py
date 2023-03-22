import core.models
from django.contrib.auth.models import User
from django.db import models


class Profile(core.models.BaseImage):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    coffee_count = models.IntegerField(verbose_name="Кол-во чашек кофе")
    birthday = models.DateField(
        verbose_name="День рождения", blank=True, null=True
    )
