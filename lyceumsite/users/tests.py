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
