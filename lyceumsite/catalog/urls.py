from django.urls import path, re_path, register_converter

from . import converters, views

app_name = "catalog"

register_converter(converters.PositiveNumberConverter, "pn")

urlpatterns = [
    path("", views.item_list, name="list"),
    path("<int:id>/", views.item_detail, name="detail"),
    re_path(r"^re/(?P<num>[1-9]\d*)/$", views.regex_num),
    path("converter/<pn:num>/", views.convert_num),
]
