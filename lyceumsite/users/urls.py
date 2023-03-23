import django.contrib.auth.views
from django.urls import path

from . import forms, views

app_name = "users"

urlpatterns = [
    path("auth/signup", views.signup, name="signup"),
    path(
        "auth/login/",
        django.contrib.auth.views.LoginView.as_view(
            template_name="users/login.html",
            form_class=forms.CustomAuthForm,
        ),
        name="login",
    ),
    path(
        "auth/logout/",
        django.contrib.auth.views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "auth/password_change/",
        django.contrib.auth.views.PasswordChangeView.as_view(
            template_name="users/pass_change.html",
            form_class=forms.CustomPassChangeForm,
        ),
        name="password_change",
    ),
    path(
        "auth/password_change/done/",
        django.contrib.auth.views.PasswordChangeDoneView.as_view(
            template_name="users/pass_change_done.html",
        ),
        name="password_change_done",
    ),
    path(
        "auth/password_reset/",
        django.contrib.auth.views.PasswordResetView.as_view(
            template_name="users/pass_reset.html",
            form_class=forms.CustomPassResetForm,
        ),
        name="password_reset",
    ),
    path(
        "auth/password_reset/done/",
        django.contrib.auth.views.PasswordResetDoneView.as_view(
            template_name="users/pass_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "auth/reset/<uidb64>/<token>/",
        django.contrib.auth.views.PasswordResetConfirmView.as_view(
            template_name="users/pass_reset_confirm.html",
            form_class=forms.CustomPassResetConfirmForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "auth/reset/done/",
        django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name="users/pass_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "auth/activate/<uidb64>/<token>/",
        views.activate,
        name="activate",
    ),
    path("users/", views.user_list, name="user_list"),
    path("my-profile/", views.user_profile, name="profile"),
    path("users/detail/<int:pk>", views.user_detail, name="user_detail"),
]
