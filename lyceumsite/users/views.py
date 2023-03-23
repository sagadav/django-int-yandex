import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
import django.utils.encoding
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from . import forms, tokens


def signup(request):
    form = forms.SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = settings.USER_IS_ACTIVE or settings.DEBUG
        user.save()
        email = form.cleaned_data["email"]
        current_site = get_current_site(request)
        message = render_to_string(
            "email/activate_email.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": tokens.user_activation_token.make_token(user),
            },
        )
        send_mail(
            "Регистрация",
            message,
            os.environ.get("FEEDBACK_EMAIL_FROM"),
            [email],
            fail_silently=False,
        )
        messages.success(
            request, "На вашу почту отправлено письмо с ссылкой для активации!"
        )
    return render(request, "users/signup.html", {"form": form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
    except django.utils.encoding.DjangoUnicodeDecodeError:
        uid = None
    user = get_object_or_404(User, pk=uid)
    done = False
    if user is not None and tokens.user_activation_token.check_token(
        user, token
    ):
        user.is_active = True
        user.save()
        login(request, user)
        done = True
    return render(request, "users/signup_activate.html", {"done": done})


def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, "users/user_list.html", {"users": users})


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, "users/user_detail.html", {"user": user})


def user_profile(request):
    form = forms.ProfileForm(instance=request.user)
    if request.POST:
        if "coffee" in request.POST:
            request.user.profile.coffee_count += 1
            request.user.save()
        else:
            form = forms.ProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save(commit=False)
                request.user.profile.birthday = form.cleaned_data["birthday"]
                request.user.profile.image = form.cleaned_data["image"]
                request.user.save()
    return render(
        request,
        "users/user_profile.html",
        {"form": form, "coffee_count": request.user.profile.coffee_count},
    )
