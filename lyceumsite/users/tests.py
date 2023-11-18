from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse
from freezegun import freeze_time


class UsersTests(TestCase):
    def test_signup(self):
        form_data = {
            "email": "test@mail.ru",
            "username": "test-uniq-test",
            "password1": "123a",
            "password2": "123a",
        }
        response = Client().post(reverse("users:signup"), data=form_data)
        self.assertIn("form", response.context)
        self.assertEqual(len(mail.outbox), 1)

    def test_signup_activate_expire(self):
        form_data = {
            "email": "test@mail.ru",
            "username": "test-uniq-test",
            "password1": "123a",
            "password2": "123a",
        }
        Client().post(reverse("users:signup"), data=form_data)
        uid, token, _ = (
            str(mail.outbox[0].message()).split("activate/")[1].split("/")
        )
        response_activate = Client().get(
            reverse("users:activate", args=[uid, token])
        )
        self.assertTrue(response_activate.context["done"])

    def test_login(self):
        user = User.objects.create(
            email="test@hello.com",
            username="test",
            is_active=True,
        )
        user.set_password("123a")
        user.save()
        form_data = {
            "username": "test",
            "password": "123a",
        }
        response = Client().post(
            reverse("users:login"), data=form_data, follow=True
        )
        self.assertRedirects(response, "/")
        self.assertIn("user", response.context)
        self.assertEqual(response.context["user"].username, "test")
        
    @freeze_time("2012-01-14")
    def test_signup_activate_expire(self):
        form_data = {
            "email": "test@mail.ru",
            "username": "test-uniq-test",
            "password1": "123a",
            "password2": "123a",
        }
        Client().post(reverse("users:signup"), data=form_data)
        uid, token, _ = (
            str(mail.outbox[0].message()).split("activate/")[1].split("/")
        )
        with freeze_time(datetime.now() + timedelta(hours=12, seconds=1)):
            response_activate = Client().get(
                reverse("users:activate", args=[uid, token])
            )
            self.assertFalse(response_activate.context["done"])
