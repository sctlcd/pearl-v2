from django.urls import path
from . import views


# Home urls

urlpatterns = [
    path('', views.index, name='home'),
]
