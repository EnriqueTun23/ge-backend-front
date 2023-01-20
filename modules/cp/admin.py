from django.contrib import admin
from .models import CodigoPostales
# Register your models here.

@admin.register(CodigoPostales)
class ViewAdminCodigoPostal(admin.ModelAdmin):
    list_display = ('codigo_postal', 'municipio')
