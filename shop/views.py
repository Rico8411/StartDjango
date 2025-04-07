from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def product(request):
    return render(request, "product.html")


def store(request):
    return render(request, "store.html")


def hekout(request):
    return render(request, "hekout.html")
