from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User


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
