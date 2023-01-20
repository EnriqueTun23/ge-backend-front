"""Url api codigo postales """
from django.urls import path
from .views import ApiCPView

urlpatterns = [
    path('', ApiCPView.as_view(), name='codigos'),
]