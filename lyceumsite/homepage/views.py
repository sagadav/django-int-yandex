import catalog.models
from django.shortcuts import render


def home(request):
    items = (
        catalog.models.Item.objects.published()
        .filter(is_on_main=True)
        .order_by("name")
    )
    return render(request, "homepage/home.html", {"items": items})
