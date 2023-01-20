""" model Marketing"""
# Django
from django.db import models
# utils 
from modules.utils.models import BaseModel
# models
from modules.project.models import Project
from modules.files.models import MarketingFile

class Marketing(BaseModel):
    """ modelo de marketing """
    files = models.ManyToManyField(MarketingFile, related_name='files')
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.project