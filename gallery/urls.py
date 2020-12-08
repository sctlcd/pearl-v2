from django.urls import path
from . import views


# Gallery urls

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('/share', views.gallery_share, name='gallery_share'),
]
