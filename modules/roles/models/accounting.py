""" model cost"""
# Django
from django.db import models
# utils 
from modules.utils.models import BaseModel
# models
from modules.project.models import Project
from modules.files.models import AccountingFile

class Accounting(BaseModel):
    """ modelo Residente de obra """
    payment_number = models.IntegerField(verbose_name='Pago inicial', default=0)
    date = models.DateField(verbose_name='Fecha de pago')
    statement_payment = models.BooleanField(verbose_name='estado de pago', default=False)
    amount = models.DecimalField(verbose_name='Cantidad', max_digits=11, decimal_places=4)
    files = models.ManyToManyField(AccountingFile, related_name='files')
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return '{}, numero de pago {}'.format(self.project, self.payment_number)