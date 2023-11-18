import core.models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProxyUserManager(models.Manager):
    def all(self):
        return super().filter(is_active=True).select_related("profile")


class ProxyUser(User):
    objects = ProxyUserManager()

    class Meta:
        proxy = True


class Profile(core.models.BaseImage):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="profile",
    )
    coffee_count = models.IntegerField(
        verbose_name="Кол-во чашек кофе", default=0
    )
    birthday = models.DateField(
        verbose_name="День рождения", blank=True, null=True
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
