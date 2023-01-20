""" Django model utils """

# Django
from django.db import models

class BaseModel(models.Model):
    """ Clase base para todos aquellos modelos que necesiten fecha de creacion y actualizacion"""

    created = models.DateTimeField(verbose_name="Fecha de creacion", auto_now_add=True, help_text="El el tiempo en que el objeto fue creado")
    update = models.DateTimeField(verbose_name="Fecha de actualizacion", auto_now=True, help_text="Es el tiempo en que el objeto se actualizo")

    class Meta:
        """ Meta Base model """
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
