
# Create your models here.
""" Model file image """
# Django
from django.db import models
from django.utils.timezone import now
# Utils model
from modules.utils.models import BaseModel
# models
from modules.users.models import User
from modules.files.models import ImageProject

class Project(BaseModel):
    """ modelo projecto """
    user = models.ManyToManyField(User, related_name='users')
    name_project = models.CharField(verbose_name="Nombre del proyecto", max_length= 255)
    street = models.CharField(verbose_name='Calle', max_length=255, blank=True, null=True)
    interior_number = models.CharField(verbose_name='Numero interior', max_length=7, blank=True, null=True)
    outdoor_number = models.CharField(verbose_name='Numero exterior', max_length=7, blank=True, null=True)
    cp = models.CharField(verbose_name='Codigo postal', max_length=16)
    suburn = models.CharField(verbose_name='Colonia', max_length=255)
    location = models.CharField(verbose_name='localidad', max_length=255)
    municipality = models.CharField(verbose_name='Municipio', max_length=255)
    estado = models.CharField(verbose_name='Estado', max_length=255)
    latitude = models.FloatField(verbose_name='Latitud', max_length=255, blank=True, null=True)
    longitud = models.FloatField(verbose_name='longitud', max_length=255, blank=True, null=True)
    photos = models.ManyToManyField(ImageProject, related_name='photos')
    
    class Meta:
        ordering = ('created', 'update')

    def __str__(self):
        return self.name_project