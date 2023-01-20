""" model juridical"""
# Django
from django.db import models
# utils 
from modules.utils.models import BaseModel
# models
from modules.project.models import Project
from modules.files.models import JuridicalFile
from .tramit_of_project import TramitOfProject

class Juridical(BaseModel):
    """ modelo de juridico """
    files = models.ManyToManyField(JuridicalFile, related_name='files')
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    tramits = models.ManyToManyField(TramitOfProject, related_name='tramites')
    
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.project