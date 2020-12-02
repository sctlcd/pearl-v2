from django.urls import path
from . import views


# Checkout urls


urlpatterns = [
    path('', views.checkout, name='checkout')
]
