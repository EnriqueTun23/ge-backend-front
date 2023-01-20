# Django 
from django.core.management.base import BaseCommand
# models
from modules.cp.models import CodigoPostales
 # pandas
import pandas as pd


class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        postales = CodigoPostales.objects.all()
        postales.delete()