""" Views administrative client panel """

# Django 
from django.views.generic import ListView
# Utils
from modules.utils.mixins import AuthMixin
# models 
from .models import Cliente

# Django REST Framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
# Serializers
from .serializers import ClientSerializer


# Create your views here.

""" ----- CRUD Client ----- """

class ClientListView(AuthMixin, ListView):
    """ List client """
    template_name = 'clients/administrador/clients.html'
    context_object_name = 'clients'
    model = Cliente


class ClientAPI(ListCreateAPIView):
    model = Cliente
    queryset = Cliente.objects.all()
    serializer_class =  ClientSerializer
    permission_classes = (IsAuthenticated,)


class ClientUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    queryset = Cliente
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    

