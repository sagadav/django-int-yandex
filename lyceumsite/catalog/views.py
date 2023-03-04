from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    return render(request, "catalog/catalog.html")


def item_detail(request, id):
    return render(request, "catalog/detail.html")


def regex_num(request, num):
    return HttpResponse(f"<body>{num}</body>")


def convert_num(request, num):
    return HttpResponse(f"{num + num}")
