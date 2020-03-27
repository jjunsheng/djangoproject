from django.urls import path
from . import views


# /products
# /products/1/details
urlpatterns = [
    path('', views.index)
]