""" Urls User """

# Django
from django.urls import path
# Views Users
from .views import ClientListView, ClientAPI, ClientUpdateDeleteAPI

urlpatterns = [
    # client  CRUD
    path('', ClientAPI.as_view(), name='clients_api'),
    path('list/', ClientListView.as_view(), name='clientList'),
    path('<int:pk>/', ClientUpdateDeleteAPI.as_view(), name='client_udpate_delete'),
]