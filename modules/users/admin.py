from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User, UserRol, UserPerson

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'is_verified', )
    list_filter = ('email', 'is_verified', 'created',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Extra', {'fields': ('phone_number', 'is_verified', 'first_name', 'last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'phone_number', 'is_verified', 'first_name', 'last_name')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

@admin.register(UserRol)
class UserRolAdmin(admin.ModelAdmin):
    list_display = ('position', )


@admin.register(UserPerson)
class UserPersonAdmin(admin.ModelAdmin):
    list_display = ('employee', )

admin.site.register(User, CustomUserAdmin)