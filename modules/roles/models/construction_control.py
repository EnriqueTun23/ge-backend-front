""" model construction control"""
# Django
from django.db import models
# utils 
from modules.utils.models import BaseModel
# models
from modules.project.models import Project
from modules.files.models import ConstructionFile

class ConstructionControl(BaseModel):
    """ modelo Control de construccion """
    files = models.ManyToManyField(ConstructionFile, related_name='files')
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.project