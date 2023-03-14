import catalog.models
from django.test import Client, TestCase
import django.urls
from parameterized import parameterized


class StaticURLTests(TestCase):
    def test_homepage(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)


class ItemsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name="cc",
            slug="test-category-slug",
            weight=100,
        )

    def test_homepage_correct_context(self):
        catalog.models.Item.objects.create(
            is_on_main=True,
            is_published=True,
            name="test-item",
            text="превосходно",
            category=self.category,
        )
        response = django.test.Client().get(django.urls.reverse("home:index"))
        self.assertIn("items", response.context)
        self.assertEqual(response.context["items"].count(), 1)

    def test_homepage_filter_is_not_on_main(self):
        catalog.models.Item.objects.create(
            is_published=True,
            name="test-item",
            text="превосходно",
            category=self.category,
        )
        response = django.test.Client().get(django.urls.reverse("home:index"))
        self.assertIn("items", response.context)
        self.assertEqual(response.context["items"].count(), 0)

    @parameterized.expand(
        [
            (("a", "b", "c"), (1, 2, 3)),
            (("b", "a", "c", "d"), (2, 1, 3, 4)),
            (("c", "a", "b"), (2, 3, 1)),
        ]
    )
    def test_items_orderby_name(self, items_names, expecting_ids):
        for i in items_names:
            catalog.models.Item.objects.create(
                is_on_main=True,
                is_published=True,
                name=i,
                text="превосходно",
                category=self.category,
            )
        response = django.test.Client().get(django.urls.reverse("home:index"))
        self.assertTupleEqual(
            tuple(map(lambda x: x.id, response.context["items"])),
            expecting_ids,
        )
