from django.urls import path
from . import views


# Gallery urls

urlpatterns = [
    path('', views.gallery, name='gallery'),
]
