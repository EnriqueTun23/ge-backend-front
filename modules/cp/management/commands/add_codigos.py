# django 
from django.core.management.base import BaseCommand
# pandas
import pandas as pd
# models
from modules.cp.models import CodigoPostales

# https://www.youtube.com/watch?v=nc4kB3HxjiA
# trabajar los xls len(data)
class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
       
        xls = pd.ExcelFile('codigos.xls') 
        
        for index, row in xls.parse('Aguascalientes').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Aguascalintes guardado')

        for index, row in xls.parse('Baja_California').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Baja california guardado')

        for index, row in xls.parse('Baja_California_Sur').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Baja california sur guardado')
        
        for index, row in xls.parse('Campeche').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Guardado Campeche')
        
        for index, row in xls.parse('Coahuila_de_Zaragoza').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Cuahuila guardado')

        for index, row in xls.parse('Colima').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Colima guardado')

        for index, row in xls.parse('Chiapas').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Chiapas guardado')

        for index, row in xls.parse('Chihuahua').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Chihuahua guardado')

        for index, row in xls.parse('Distrito_Federal').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('CDMX guardado')

        for index, row in xls.parse('Durango').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Durango guardado')
        
        for index, row in xls.parse('Guanajuato').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Guanajuato Guardado')

        for index, row in xls.parse('Guerrero').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Guerrero Guardado')

        for index, row in xls.parse('Hidalgo').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Hidalgo Guardado')

        for index, row in xls.parse('Jalisco').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Jalisco Guardado')

        for index, row in xls.parse('M??xico').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Mexico Guardado')

        for index, row in xls.parse('Michoac??n_de_Ocampo').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Michoacan Guardado')

        for index, row in xls.parse('Morelos').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Morelos Guardado')

        for index, row in xls.parse('Nayarit').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Nayarit Guardado')


        for index, row in xls.parse('Nuevo_Le??n').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Nuevo_Le??n Guardado')

        for index, row in xls.parse('Oaxaca').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Oaxaca Guardado')

        for index, row in xls.parse('Puebla').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Puebla Guardado')

        for index, row in xls.parse('Quer??taro').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Quer??taro Guardado')

        for index, row in xls.parse('Quintana_Roo').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Quintana Roo Guardado')

        for index, row in xls.parse('San_Luis_Potos??').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('San_Luis_Potos?? Guardado')

        for index, row in xls.parse('Sinaloa').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Sinaloa Guardado')

        for index, row in xls.parse('Sonora').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Sonora Guardado')

        for index, row in xls.parse('Tabasco').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Tabasco Guardado')

        for index, row in xls.parse('Tamaulipas').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Tamaulipas Guardado')

        for index, row in xls.parse('Tlaxcala').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Tlaxcala Guardado')

        for index, row in xls.parse('Veracruz_de_Ignacio_de_la_Llave').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Veracruz Guardado')

        for index, row in xls.parse('Yucat??n').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Yucat??n Guardado')

        for index, row in xls.parse('Zacatecas').iterrows():
            x = CodigoPostales(codigo_postal=row[0], asentamiento=row[1], tipo_asentamiento=row[2], municipio=row[3], estado=row[4], ciudad=row[5])
            try:
                x.save()
            except:
                print('Hubo error')
        print('Zacatecas Guardado')
