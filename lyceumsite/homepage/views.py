from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "homepage/home.html")


def coffee(request):
    return HttpResponse("<body>Я чайник</body>", status=418)
