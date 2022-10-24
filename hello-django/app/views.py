import random
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def hello_world(request) -> HttpResponse:
    return HttpResponse("Hello World!")


# def hello_views(request, name) -> HttpResponse:
#     return HttpResponse(f"Hello, {name}")


# def roll_die_view(request, sides):
#     roll = random.randint(1, (int(sides)))
#     return HttpResponse(roll)


# def random_between_view(request, lo, hi):
#     return HttpResponse(random.randint(lo, hi))
