import os

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from . import forms, models


def feedback(request):
    form = forms.FeedbackForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        text = form.cleaned_data["text"]
        mail = form.cleaned_data["mail"]
        feedback_model = models.Feedback(mail=mail, text=text)
        feedback_model.save()
        send_mail(
            "Subject here",
            text,
            os.environ.get("FEEDBACK_EMAIL_FROM"),
            [mail],
            fail_silently=False,
        )
        return redirect(reverse("feedback:thankyou"))
    return render(request, "feedback/feedback.html", context)


def thankyou(request):
    return render(request, "feedback/thankyou.html")
