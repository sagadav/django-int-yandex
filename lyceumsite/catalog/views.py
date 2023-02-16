from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, id):
    return HttpResponse(f"Подробно элемент {id}")


def regex_num(request, num):
    return HttpResponse(f"<body>{num}</body>")


def convert_num(request, num):
    return HttpResponse(f"<body>{num + num}</body>")
