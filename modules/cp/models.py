# Models Codigos postales
from django.db import models

class CodigoPostales(models.Model):
    codigo_postal = models.IntegerField(blank=True, null=True)
    asentamiento = models.CharField(max_length=255, blank=True, null=True)
    tipo_asentamiento = models.CharField(max_length=255, blank=True, null=True)
    municipio = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.codigo_postal


