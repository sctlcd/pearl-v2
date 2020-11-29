from django.urls import path
from . import views


# Products urls

urlpatterns = [
    path('', views.all_products, name='products'),
]
