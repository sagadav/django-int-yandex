from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_list(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_detail(self):
        response = Client().get("/catalog/2/")
        self.assertEqual(response.status_code, 200)

    def test_regex_num(self):
        response = Client().get("/catalog/re/2/")
        self.assertEqual(response.status_code, 200)

    def test_regex_num_string(self):
        response = Client().get("/catalog/re/awdawd/")
        self.assertEqual(response.status_code, 404)

    def test_num_converter(self):
        response = Client().get("/catalog/converter/2/")
        self.assertEqual(response.status_code, 200)

    def test_num_converter_string(self):
        response = Client().get("/catalog/converter/awdwadw/")
        self.assertEqual(response.status_code, 404)
