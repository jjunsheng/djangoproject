from django.shortcuts import render
from django.http import HttpResponse


# /product -> url mapping
# URL = Uniform Resource Locator(Address)

# main page of an app is always called index
def index(request):
    return HttpResponse("Hello World")