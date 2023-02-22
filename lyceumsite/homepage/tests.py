from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_coffee(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)
