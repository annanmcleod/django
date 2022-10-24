from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def hey_views(request, name) -> HttpResponse:
    return HttpResponse(f"Hello, {name}!")


def how_old(request, end, birthyear):
    age = end - birthyear
    return HttpResponse(age)


def take_order(request, burgers, fries, drinks):
    bt = burgers * 4.50
    ft = fries * 1.5
    dt = drinks * 1
    total = bt + ft + dt
    return HttpResponse(f"$" + str(total))
