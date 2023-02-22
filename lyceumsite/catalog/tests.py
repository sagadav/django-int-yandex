import catalog.models
import django.core.exceptions
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


class ModelsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name="test",
            slug="test-category-slug",
            weight=100,
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="test",
            slug="test-tag-slug",
        )

    def test_unable_create_without_specific_words(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            item = catalog.models.Item(
                name="test_item", text="22", category=self.category
            )
            item.full_clean()
            item.save()
        self.assertEqual(catalog.models.Item.objects.count(), item_count)

    @parameterized.expand(
        [("test_item", "превосходно"), ("test_item", "роскошно")]
    )
    def test_create_item(self, name, text):
        item_count = catalog.models.Item.objects.count()
        item = catalog.models.Item(
            name=name,
            text=text,
            category=self.category,
        )
        item.full_clean()
        item.save()
        item.tags.add(self.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count + 1,
            f"{name}, {text}",
        )

    @parameterized.expand(
        [
            ("test_tag", "test-@-slug"),
            ("test_tag", "test-#-hello"),
            ("test_tag", "тест"),
        ]
    )
    def test_tag_wrong_slug(self, name, slug):
        item_count = catalog.models.Tag.objects.count()
        with self.assertRaises(
            django.core.exceptions.ValidationError, msg=f"{name}, {slug}"
        ):
            item = catalog.models.Tag(name=name, slug=slug)
            item.full_clean()
            item.save()
        self.assertEqual(catalog.models.Tag.objects.count(), item_count)

    def test_create_tag(self):
        item_count = catalog.models.Tag.objects.count()
        tag = catalog.models.Tag(
            name="test_item",
            slug="test-1234567890-slug",
        )
        tag.full_clean()
        tag.save()
        self.assertEqual(catalog.models.Tag.objects.count(), item_count + 1)
