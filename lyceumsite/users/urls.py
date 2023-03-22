import django.contrib.auth.views
from django.urls import path

from . import forms, views

app_name = "users"

urlpatterns = [
    path("signup", views.signup),
    path(
        "login/",
        django.contrib.auth.views.LoginView.as_view(
            template_name="users/login.html",
            form_class=forms.CustomAuthForm,
        ),
        name="login",
    ),
    path(
        "password_change/",
        django.contrib.auth.views.PasswordChangeView.as_view(
            template_name="users/pass_change.html",
            form_class=forms.CustomPassChangeForm,
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        django.contrib.auth.views.PasswordChangeDoneView.as_view(
            template_name="users/pass_change_done.html",
        ),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        django.contrib.auth.views.PasswordResetView.as_view(
            template_name="users/pass_reset.html",
            form_class=forms.CustomPassResetForm,
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        django.contrib.auth.views.PasswordResetDoneView.as_view(
            template_name="users/pass_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        django.contrib.auth.views.PasswordResetConfirmView.as_view(
            template_name="users/pass_reset_confirm.html",
            form_class=forms.CustomPassResetConfirmForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name="users/pass_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "activate/",
        django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name="users/pass_reset_complete.html"
        ),
        name="activate",
    ),
]
