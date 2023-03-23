from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse


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
