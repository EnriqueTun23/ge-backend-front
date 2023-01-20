""" Model tramite of project"""
# Django
from django.db import models
# Utils
from modules.utils.models import BaseModel
MANAGEMENT = [
    ('MUNICIPAL', 'Municipal'),
    ('FEDERAL', 'Federal'),
    ('ESTATAL', 'Estatal'),
    ('MISCELANEO','Misceláneo')
]

class TramitOfProject(BaseModel):
    name = models.CharField(verbose_name='Nombre del archivo', max_length=255)
    management = models.CharField(verbose_name='Administrativo', max_length=25, choices=MANAGEMENT, default='FEDERAL')
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return 'nombre: {}, tipo de documento {}'.format(self.name, self.management)