from django.urls import path
from . import views


# Contact urls

urlpatterns = [
    path('', views.contact, name='contact')
]
