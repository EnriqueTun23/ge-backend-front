""" Admin client """
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Models
from .models import Cliente



@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rfc', 'created')

