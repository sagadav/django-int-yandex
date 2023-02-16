from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.item_list),
    path("<int:id>/", views.item_detail),
    re_path(r"re/(?P<num>\d+)/", views.regex_num),
    path("converter/<int:num>/", views.convert_num),
]
