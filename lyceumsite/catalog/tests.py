from django.test import Client, TestCase

from parameterized import parameterized


class StaticURLTests(TestCase):
    @parameterized.expand(
        [
            ("", 200),
            ("re/2/", 200),
            ("re/awdaw/", 404),
            ("re/004/", 404),
            ("converter/23/", 200),
            ("converter/awd/", 404),
            ("converter/002/", 404),
        ]
    )
    def test_catalog_endpoints(self, endpoint, expected_status_code):
        response = Client().get(f"/catalog/{endpoint}")
        self.assertEqual(
            response.status_code,
            expected_status_code,
            f"Endpoint: {endpoint}",
        )
