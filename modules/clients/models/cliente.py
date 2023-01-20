""" Model Cliente """

# Django
from django.db import models
from django.core.validators import RegexValidator
# Models
from modules.users.models import UserRol
from modules.project.models import Project
# Utils
from modules.utils.models import BaseModel

class Cliente(BaseModel):
    business_name = models.CharField(verbose_name="Razon social", max_length=255)
    rfc = models.CharField(verbose_name="RFC", max_length=14)
    # company_name = models.CharField(verbose_name="Nombre de la empresa", max_length=255)
    street = models.CharField(verbose_name='Calle', max_length=255, blank=True, null=True)
    interior_number = models.CharField(verbose_name='Numero interior', max_length=7, blank=True, null=True)
    outdoor_number = models.CharField(verbose_name='Numero exterior', max_length=7, blank=True, null=True)
    cp = models.CharField(verbose_name='Codigo postal', max_length=16)
    suburn = models.CharField(verbose_name='Colonia', max_length=255)
    location = models.CharField(verbose_name='localidad', max_length=255)
    municipality = models.CharField(verbose_name='Municipio', max_length=255)
    estado = models.CharField(verbose_name='Estado', max_length=255)

    email_business = models.EmailField(verbose_name="Email razon social")

    phone_regex = RegexValidator(regex=r'(\(\+?\d{2,3}\)[\*|\s|\-|\.]?(([\d][\*|\s|\-|\.]?){6})(([\d][\s|\-|\.]?){2})?|(\+?[\d][\s|\-|\.]?){8}(([\d][\s|\-|\.]?){2}(([\d][\s|\-|\.]?){2})?)?)$', message="Numero telefonico debe ser entero en el formato: (+52) 9991254545 ,999-992-9845 o (999) 123 1456. Puedes usar 15 digitos maximo.")
    phone_number_bussiness = models.CharField( verbose_name="Telefono razon social", blank=True, null=True, max_length= 25, validators=[phone_regex])

    ext = models.IntegerField(verbose_name="Extension telefono", blank=True, null=True) 

    users = models.ManyToManyField(UserRol, related_name='users')
    """ User-login en los formularios hay que traer los user y mandar el pk  de login en select"""
    projects = models.ManyToManyField(Project, related_name='projects')

    class Meta:
        ordering = ('created', 'rfc')

    def __str__(self):
        return 'RFC: {} - Razon social: {}'.format(self.rfc, self.business_name)


