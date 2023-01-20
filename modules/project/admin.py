from django.contrib import admin

# Register your models here.

# Models
from .models import Project

@admin.register(Project)
class ConstructionAdmin(admin.ModelAdmin):
    pass