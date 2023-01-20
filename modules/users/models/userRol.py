""" Model UserRol """

# Django
from django.db import models

# Utils
from modules.utils.models import BaseModel

class UserRol(BaseModel):
    POSITIONS = [
        ('GE Costos', 'Costos'),
        ('GE Contabilidad', 'Contabilidad'),
        ('GE Tramitologia', 'Tramitologia'),
        ('GE Estimaciones', 'Estimaciones'),
        ('GE Compras', 'Compras'),
        ('GE Avance de Obra', 'Avance de Obra'),
        ('GE Programa de obra', 'Programa de obra'),
        ('GE Residente', 'Residente'),
        ('Supervisor Avance de obra', 'Supervisor Avance de obra'),
        ('Supervisor Programa de obra', 'Supervisor Programa de obra'),
        ('Cliente', 'Cliente'),
        ('Director', 'Director'),
        ('Administrador', 'Administrador')
    ]
    position = models.CharField(verbose_name='Cargo', max_length=50, choices=POSITIONS)
    cost = models.BooleanField(verbose_name='Rol costos', default=False)
    accounting = models.BooleanField(verbose_name='Rol contabilidad', default=False)
    tramitology = models.BooleanField(verbose_name='Rol tramitologia', default=False)
    estimation = models.BooleanField(verbose_name='Rol estimaciones', default=False)
    shopping = models.BooleanField(verbose_name='Rol compras', default=False)
    construction_advance = models.BooleanField(verbose_name='Rol avances de obras', default=False)
    construction_program = models.BooleanField(verbose_name='Rol programa de obra', default=False)
    resident = models.BooleanField(verbose_name='Rol Residente', default=False)

    class Meta:
        ordering = ('-position',)

    def __str__(self):
        return self.position