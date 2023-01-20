from django.shortcuts import render
from django.views.generic import CreateView
# forms
from modules.files.forms import ImageProjectCreate
# Serializer
from .serializers import ImageProjectSerializer
# Django Rest Framework
from rest_framework.generics import  ListCreateAPIView
# models
from .models import ImageProject


# Create your views here.
class CreateImgProjectUpdateView(CreateView):
    template_name = 'modals/img_project.html'
    form_class= ImageProjectCreate
    #success_url =  reverse_lazy('userList')


class ImageProjectAPI(ListCreateAPIView):
    model = ImageProject
    queryset = ImageProject.objects.all()
    serializer_class = ImageProjectSerializer