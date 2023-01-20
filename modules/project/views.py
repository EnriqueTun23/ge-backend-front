from django.shortcuts import render

# Create your views here.
# Utils
from modules.utils.mixins import AuthMixin
# Django 
from django.views.generic import ListView
# Models
from .models import Project
from modules.users.models import User
# Django REST Framework
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
# Serializer
from .serializer import ProjectSerializer



class ProjectsListView(AuthMixin, ListView):
    """ List project """
    template_name = 'adminstrador_project/projects.html'
    context_object_name = 'projects'
    model = Project

    def get_context_data(self, **kwargs):
        datos =  super(ProjectsListView, self).get_context_data(**kwargs)
        datos['users_many'] = User.objects.filter(userPerson__employee=True)
        return datos
    
    
class ProjectAPI(ListCreateAPIView):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    

class ProjectUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    queryset = Project
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
