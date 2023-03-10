# Generated by Django 2.1.5 on 2020-03-09 22:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='El el tiempo en que el objeto fue creado', verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, help_text='Es el tiempo en que el objeto se actualizo', verbose_name='Fecha de actualizacion')),
                ('business_name', models.CharField(max_length=255, verbose_name='Razon social')),
                ('rfc', models.CharField(max_length=14, verbose_name='RFC')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='Calle')),
                ('interior_number', models.CharField(blank=True, max_length=7, null=True, verbose_name='Numero interior')),
                ('outdoor_number', models.CharField(blank=True, max_length=7, null=True, verbose_name='Numero exterior')),
                ('cp', models.CharField(max_length=16, verbose_name='Codigo postal')),
                ('suburn', models.CharField(max_length=255, verbose_name='Colonia')),
                ('location', models.CharField(max_length=255, verbose_name='localidad')),
                ('municipality', models.CharField(max_length=255, verbose_name='Municipio')),
                ('estado', models.CharField(max_length=255, verbose_name='Estado')),
                ('email_business', models.EmailField(max_length=254, verbose_name='Email razon social')),
                ('phone_number_bussiness', models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.RegexValidator(message='Numero telefonico debe ser entero en el formato: (+52) 9991254545 ,999-992-9845 o (999) 123 1456. Puedes usar 15 digitos maximo.', regex='(\\(\\+?\\d{2,3}\\)[\\*|\\s|\\-|\\.]?(([\\d][\\*|\\s|\\-|\\.]?){6})(([\\d][\\s|\\-|\\.]?){2})?|(\\+?[\\d][\\s|\\-|\\.]?){8}(([\\d][\\s|\\-|\\.]?){2}(([\\d][\\s|\\-|\\.]?){2})?)?)$')], verbose_name='Telefono razon social')),
                ('ext', models.IntegerField(blank=True, null=True, verbose_name='Extension telefono')),
                ('projects', models.ManyToManyField(related_name='projects', to='project.Project')),
                ('users', models.ManyToManyField(related_name='users', to='users.UserRol')),
            ],
            options={
                'ordering': ('created', 'rfc'),
            },
        ),
    ]
