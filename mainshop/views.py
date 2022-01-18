from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("mainshop application")


def main(request):
    return render(request, 'mainshop/index.html')


def products(request):
    return render(request, 'mainshop/products.html')


def contact(request):
    return render(request, 'mainshop/contact.html')
