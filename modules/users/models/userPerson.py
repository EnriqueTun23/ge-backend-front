""" Model Person """

# Django
from django.db import models
# Utils
from modules.utils.models import BaseModel

class UserPerson(BaseModel):
    client = models.BooleanField(verbose_name='Cliente', default=False)
    supervisor_pdo = models.BooleanField(verbose_name='Supervisor de programa de obra', default=False)
    supervisor_ado = models.BooleanField(verbose_name='Supervisor de avances de obra', default=False)
    employee = models.BooleanField(verbose_name='Empleado', default=False)
    director = models.BooleanField(verbose_name='Director', default=False)
    management = models.BooleanField(verbose_name='Administrador', default=False)

    class Meta:
        ordering = ('employee',)