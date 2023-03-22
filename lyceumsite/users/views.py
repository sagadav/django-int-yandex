from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
import os
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.conf import settings

from . import forms, tokens


def signup(request):
    form = forms.SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = os.environ.get("USER_IS_ACTIVE", default=('true' if settings.DEBUG else 'false')) in (
            'true', 'True')
        email = form.cleaned_data["email"]
        current_site = get_current_site(request)
        message = render_to_string(
            "email/activate_email.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": tokens.user_activation_token.make_token(user)
            },
        )
        send_mail(
            "Регистрация",
            message,
            os.environ.get("FEEDBACK_EMAIL_FROM"),
            [email],
            fail_silently=False,
        )
    return render(request, "users/signup.html", {"form": form})


def activate(request, uidb64, token):
    return "awdw"
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        print(e)
        return "Hello"
    done = False
    if user is not None and tokens.user_activation_token.check_token((user, token)):
        user.is_active = True
        user.save()
        login(request, user)
        done = True
    return render(request, "users/signup_activate.html", {"done": done})
