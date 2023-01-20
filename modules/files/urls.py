""" Urls core """

from django.urls import path, include
from .views import ImageProjectAPI

urlpatterns = [
    # prueba
    path('create/img/', ImageProjectAPI.as_view(), name='puebaprojectoImg'),
]
