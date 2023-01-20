# Django 
from django.core.management.base import BaseCommand
# pandas
import pandas as pd
# models
from modules.cp.models import CodigoPostales

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        xls = pd.ExcelFile('codigos.xls')
        
        for estado in xls.sheet_names:
            if estado != 'Nota':
                for row in xls.parse(estado).iterrows():
                    CodigoPostales(codigo_postal=row[1].d_codigo, asentamiento=row[1].d_asenta, tipo_asentamiento=row[1].d_tipo_asenta, municipio=row[1].D_mnpio, estado=row[1].d_estado, ciudad=row[1].d_ciudad).save()
                    # x = CodigoPostales(codigo_postal=row[1].d_codigo, asentamiento=row[1].d_asenta, tipo_asentamiento=row[1].d_tipo_asenta, municipio=row[1].D_mnpio, estado=row[1].d_estado, ciudad=row[1].d_ciudad)
                    # try:
                    #     x.save()
                    # except:
                    #     print('Hubo error')
                    

        print('cp Guardados')            
            
        
                    # print('codigo_postal= {} | asentamiento= {} | tipo_asentamiento={} | municipio={} | estado={} | ciudad={}'.format(row[1].d_codigo, row[1].d_asenta, row[1].d_tipo_asenta, row[1].D_mnpio, row[1].d_estado, row[1].d_ciudad))
                    