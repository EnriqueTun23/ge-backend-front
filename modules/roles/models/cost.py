""" model cost"""
# Django
from django.db import models
# utils 
from modules.utils.models import BaseModel
# models
from modules.project.models import Project

class Cost(BaseModel):
    initial_budget = models.DecimalField(verbose_name='Presupeusto inicial', max_digits=11, decimal_places=4)
    extraordinary_budget = models.DecimalField(verbose_name='Gasto extras', max_digits=11, decimal_places=4)
    total_cost = models.DecimalField(verbose_name='Total', max_digits=11, decimal_places=4)
    project =  models.OneToOneField(Project, on_delete=models.CASCADE)

    class Meta:
        ordering = ('project__name_project', 'project__initial_budget')
    
    def __str__(self):
        return 'Projecto {}, presupuesto inicial {}'.format(self.project.name_project, self.initial_budget)