from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request: HttpRequest):
    return HttpResponse("Hello, world. You're at the hello index.")


def some(request: HttpRequest):
    return HttpResponse("some text")


def greet(request: HttpRequest, name: str):
    return HttpResponse(f"Hello, {name.capitalize()}!")
