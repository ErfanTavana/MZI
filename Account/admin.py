# admin.py
from django.contrib import admin
from .models import AdminMZI

class AdminMZIAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_admin', 'first_name', 'last_name', 'role_name', 'profile_image']
    search_fields = ['user__username', 'first_name', 'last_name', 'role_name']
    list_filter = ['is_admin']

admin.site.register(AdminMZI, AdminMZIAdmin)