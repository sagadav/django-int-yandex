import catalog.models
import django.core.exceptions
from django.test import Client, TestCase
import django.urls
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
        cls.item = catalog.models.Item.objects.create(
            is_published=True,
            name="test-item-098",
            text="превосходно",
            category=cls.category,
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
        [
            "превосходно",
            "роскошно",
            "тест, превосходно!",
            "test, роскошно,  тест!",
            " превосходно ",
            "но роскошно ли?",
        ]
    )
    def test_create_item_text(self, text):
        item_count = catalog.models.Item.objects.count()
        item = catalog.models.Item(
            name="test_item",
            text=text,
            category=self.category,
        )
        item.full_clean()
        item.save()
        item.tags.add(self.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count + 1,
            f"{text}",
        )

    @parameterized.expand(
        ["превосходное", "роскошное", "тест", "№превосходно_"]
    )
    def test_create_item_wrong_text(self, text):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(
            django.core.exceptions.ValidationError, msg=f"{text}"
        ):
            item = catalog.models.Item(
                name="test_item",
                text=text,
                category=self.category,
            )
            item.full_clean()
            item.save()
            item.tags.add(self.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count,
            f"{text}",
        )

    def test_create_tag(self):
        item_count = catalog.models.Tag.objects.count()
        tag = catalog.models.Tag(
            name="test_tag",
            slug="test-1234567890-slug",
        )
        tag.full_clean()
        tag.save()
        self.assertEqual(catalog.models.Tag.objects.count(), item_count + 1)

    @parameterized.expand(
        [
            ("t e s t"),
            ("t#e@s_t"),
            ("t е s t"),  # cyr
            ("    test  "),
        ]
    )
    def test_normalized_name_tag_negative(self, name):
        item_count = catalog.models.Tag.objects.count()
        with self.assertRaises(
            django.core.exceptions.ValidationError, msg=f"{name}"
        ):
            item = catalog.models.Tag(name=name, slug="slug")
            item.full_clean()
            item.save()
        self.assertEqual(catalog.models.Tag.objects.count(), item_count)

    def test_create_category(self):
        item_count = catalog.models.Category.objects.count()
        tag = catalog.models.Category(
            name="test_category",
            slug="test-1234567890-slug",
        )
        tag.full_clean()
        tag.save()
        self.assertEqual(
            catalog.models.Category.objects.count(), item_count + 1
        )

    def test_catalog_correct_context(self):
        response = django.test.Client().get(
            django.urls.reverse("catalog:list")
        )
        self.assertIn("categories", response.context)
        self.assertEqual(response.context["categories"].count(), 1)

    def test_catalog_unnecessary_fields(self):
        response = django.test.Client().get(
            django.urls.reverse("catalog:list")
        )
        category = response.context["categories"][0]
        category_fields = category.__dict__
        self.assertIn("name", category_fields)
        self.assertNotIn("slug", category_fields)
        self.assertNotIn("is_published", category_fields)

        item_fields = category.catalog_items.all()[0].__dict__
        self.assertIn("name", item_fields)
        self.assertIn("text", item_fields)
        self.assertNotIn("image", item_fields)
        self.assertNotIn("is_published", item_fields)

    def test_catalog_detail_correct_context(self):
        response = django.test.Client().get(
            django.urls.reverse("catalog:detail", args=[self.item.pk])
        )
        self.assertIn("item", response.context)


class OrderTests(TestCase):
    @parameterized.expand(
        [
            (("a", "b", "c"), (1, 2, 3)),
            (("b", "a", "c", "d"), (2, 1, 3, 4)),
            (("c", "a", "b"), (2, 3, 1)),
        ]
    )
    def test_catalog_items_orderby_category(
        self, categories_names, expecting_ids
    ):
        for i in categories_names:
            category = catalog.models.Category.objects.create(
                is_published=True,
                name=i,
                slug="test-category" + i,
                weight=100,
            )
            catalog.models.Item.objects.create(
                is_published=True,
                name="test-item" + i,
                text="превосходно",
                category=category,
            )
        response = django.test.Client().get(
            django.urls.reverse("catalog:list")
        )
        self.assertTupleEqual(
            tuple(map(lambda x: x.id, response.context["categories"])),
            expecting_ids,
        )
