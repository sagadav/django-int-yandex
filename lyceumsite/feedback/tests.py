from django.test import Client, TestCase
from django.urls import reverse
from feedback.forms import FeedbackForm
from feedback.models import Feedback
from parameterized import parameterized


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
        items_count = Feedback.objects.count()
        Client().post(
            reverse("feedback:feedback"),
            data={"text": "test", "mail": "test@test.com"},
        )
        self.assertEqual(Feedback.objects.count(), items_count + 1)
        self.assertTrue(Feedback.objects.filter(mail="test@test.com").exists())

    @parameterized.expand(
        [("awd", "text"), ("", ""), ("a", ""), ("mail@mail.ru", ""), ("", "a")]
    )
    def test_feedback_form_invalid(self, mail, text):
        form = FeedbackForm(data={"text": text, "mail": mail})
        self.assertFalse(form.is_valid())
