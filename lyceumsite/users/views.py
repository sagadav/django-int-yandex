from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from . import forms


def signup(request):
    form = forms.SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        email = form.cleaned_data["email"]
        current_site = get_current_site(request)
        message = render_to_string(
            "emails/activate_email.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            },
        )
        send_mail(
            "Регистрация",
            f"Активи",
            os.environ.get("FEEDBACK_EMAIL_FROM"),
            [mail],
            fail_silently=False,
        )
    return render(request, "users/signup.html", {"form": form})
