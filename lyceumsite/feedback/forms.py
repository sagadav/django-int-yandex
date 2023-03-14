from django import forms
from . import models


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = models.Feedback
        fields = (
            models.Feedback.mail.field.name,
            models.Feedback.text.field.name,
        )
        labels = {
            models.Feedback.text.field.name: "Текст",
            models.Feedback.mail.field.name: "Эл. почта",
        }
        help_texts = {
            models.Feedback.text.field.name: "Подсказка",
        }
