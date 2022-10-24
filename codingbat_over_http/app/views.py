from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def near_hundred(request, n):
    if (abs(100 - n) <= 10) or (abs(200 - n) <= 10):
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def string_splosion(request, str):
    result = ""
    for i in range(len(str)):
        result = result + str[: i + 1]
    return HttpResponse(result)


def cat_dog(request, str):
    return HttpResponse(str.count("cat") == str.count("dog"))


def lone_sum(request, a, b, c):
    sum = 0
    if a == b or a == c or b == c:
        if a == b and a == c and b == c:
            return HttpResponse(0)
        if a == b:
            return HttpResponse(c)
        if b == c:
            return HttpResponse(a)
        if c == a:
            return HttpResponse(b)

    else:
        sum = a + b + c
        return HttpResponse(sum)
