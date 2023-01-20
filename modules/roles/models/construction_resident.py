""" model cost"""
# Django
from django.db import models
# utils 
from modules.utils.models import BaseModel
# models
from modules.project.models import Project
from modules.files.models import ConstructionResidentFile

class ConstructionResident(BaseModel):
    """ modelo Residente de obra """
    files = models.ManyToManyField(ConstructionResidentFile, related_name='files')
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.project