from django.contrib import admin

# Register your models here.

from .models import Accounting, ConstructionControl, ConstructionResident, Cost, Juridical, Marketing, TramitOfProject

@admin.register(Accounting)
class AccountingAdmin(admin.ModelAdmin):
    pass


@admin.register(ConstructionControl)
class ConstructionControlAdmin(admin.ModelAdmin):
    pass

@admin.register(ConstructionResident)
class ConstructionResidentAdmin(admin.ModelAdmin):
    pass

@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    pass

@admin.register(Juridical)
class JuridicalAdmin(admin.ModelAdmin):
    pass

@admin.register(Marketing)
class MarketingAdmin(admin.ModelAdmin):
    pass

@admin.register(TramitOfProject)
class TramitOfProjectAdmin(admin.ModelAdmin):
    pass