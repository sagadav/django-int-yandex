import catalog.models
from django.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def item_list(request):
    items = catalog.models.Item.objects.published().order_by("category__name")
    return render(request, "catalog/catalog.html", {"items": items})


def item_detail(request, id):
    queryset = (
        catalog.models.Item.objects.published()
        .prefetch_related(
            models.Prefetch(
                "item_image",
                queryset=catalog.models.ImageModel.objects.only(
                    "image", "item_id"
                ),
            )
        )
        .only("name", "text", "category__name", "image")
    )
    item = get_object_or_404(queryset, pk=id)
    return render(request, "catalog/detail.html", {"item": item})


def regex_num(request, num):
    return HttpResponse(f"<body>{num}</body>")


def convert_num(request, num):
    return HttpResponse(f"{num + num}")
