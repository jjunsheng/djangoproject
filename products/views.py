from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# /product -> url mapping
# URL = Uniform Resource Locator(Address)

# main page of an app is always called index
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new_product(request):
    return HttpResponse("New Products!")


