from django.contrib import admin

# Register your models here.
# Models
from .models import ImageProject, AccountingFile, ConstructionFile, ConstructionResidentFile, JuridicalFile, MarketingFile

@admin.register(ImageProject)
class ImageFieldProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(AccountingFile)
class AccountingFileAdmin(admin.ModelAdmin):
    pass


@admin.register(ConstructionFile)
class ConstructionFileAdmin(admin.ModelAdmin):
    pass

@admin.register(ConstructionResidentFile)
class ConstructionResidentFileAdmin(admin.ModelAdmin):
    pass

@admin.register(JuridicalFile)
class JuridicalFileAdmin(admin.ModelAdmin):
    pass

@admin.register(MarketingFile)
class MarketingFileAdmin(admin.ModelAdmin):
    pass