import catalog.models
from django.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def item_list(request):
    items = catalog.models.Item.objects.published().order_by("category__name")
    return render(request, "catalog/catalog.html", {"items": items})


def item_detail(request, id):
    queryset = (
        catalog.models.Item.objects.filter(is_published=True)
        .select_related("category")
        .prefetch_related(
            models.Prefetch(
                "tags", queryset=catalog.models.Tag.objects.all().only("name")
            )
        )
        .prefetch_related("item_image")
    )
    item = get_object_or_404(queryset, pk=id)
    return render(request, "catalog/detail.html", {"item": item})


def regex_num(request, num):
    return HttpResponse(f"<body>{num}</body>")


def convert_num(request, num):
    return HttpResponse(f"{num + num}")
