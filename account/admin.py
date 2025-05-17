from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)
    # fieldsets = (
    #     (None, {'fields': ('username', 'email', 'password')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )