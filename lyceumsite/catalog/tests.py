from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_list(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_detail(self):
        response = Client().get("/catalog/2/")
        self.assertEqual(response.status_code, 200)
