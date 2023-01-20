""" model User """
# Django
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Utils model
from modules.utils.models import BaseModel
from modules.utils.managers import CustomUserManager
# models
from modules.users.models import UserPerson, UserRol

class User(BaseModel, AbstractUser):
    username = None
    email = models.EmailField(verbose_name="email login", unique=True, error_messages = {
        'unique': 'Ya existe un usuario con este mismo correo'
    })

    phone_regex = RegexValidator(regex=r'(\(\+?\d{2,3}\)[\*|\s|\-|\.]?(([\d][\*|\s|\-|\.]?){6})(([\d][\s|\-|\.]?){2})?|(\+?[\d][\s|\-|\.]?){8}(([\d][\s|\-|\.]?){2}(([\d][\s|\-|\.]?){2})?)?)$', message="Numero telefonico debe ser entero en el formato: (+52) 9991254545 ,999-992-9845 o (999) 123 1456. Puedes usar 15 digitos maximo.")
    phone_number = models.CharField( verbose_name="Telefono", blank=True, null=True, max_length= 25, validators=[phone_regex])

    mobile_regex = RegexValidator(regex=r'(\(\+?\d{2,3}\)[\*|\s|\-|\.]?(([\d][\*|\s|\-|\.]?){6})(([\d][\s|\-|\.]?){2})?|(\+?[\d][\s|\-|\.]?){8}(([\d][\s|\-|\.]?){2}(([\d][\s|\-|\.]?){2})?)?)$', message="Numero celular debe ser entero en el formato: (+52) 9991254545 ,999-992-9845 o (999) 123 1456. Puedes usar 15 digitos maximo.")
    mobile_number = models.CharField(verbose_name="Celular", max_length=15, validators=[mobile_regex])

    ext = models.IntegerField(verbose_name="Extension telefono", default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    is_verified = models.BooleanField(verbose_name='Verificacion', default=False, help_text='Establece verdadero si el usuario tiene verficado su email')

    userRol = models.OneToOneField(UserRol, on_delete=models.CASCADE, related_name='userRol', blank=True, null=True)
    userPerson = models.OneToOneField(UserPerson, on_delete=models.CASCADE, related_name='userPerson', blank=True, null=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        """ return correo"""
        return self.email
    
    def get_short_name(self):
        """Return username."""
        return self.email