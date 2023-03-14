from django.test import Client, TestCase
from django.urls import reverse


class FeedbackTests(TestCase):
    def test_feedback_context(self):
        response = Client().get(reverse("feedback:feedback"))
        self.assertIn("form", response.context)

    def test_feedback_form_labels_help_text(self):
        response = Client().get(reverse("feedback:feedback"))
        form = response.context["form"]
        self.assertEqual(form.fields["text"].label, "Текст")
        self.assertEqual(form.fields["mail"].label, "Эл. почта")
        self.assertEqual(form.fields["text"].help_text, "Подсказка")

    def test_feedback_form(self):
        response = Client().post(
            reverse("feedback:feedback"),
            data={"text": "test", "mail": "test@test.com"},
            follow=True,
        )
        self.assertRedirects(response, reverse("feedback:thankyou"))
