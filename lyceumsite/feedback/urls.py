from django.urls import path

from . import views

app_name = "feedback"

urlpatterns = [
    path("", views.feedback, name="feedback"),
    path("thankyou/", views.thankyou, name="thankyou"),
]
