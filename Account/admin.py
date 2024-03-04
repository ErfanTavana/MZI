from django.contrib import admin
from .models import AdminMZI

class AdminMZIAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_admin')
    list_filter = ('is_admin',)
    search_fields = ('user__username', 'user__email')
    ordering = ('user__username',)

admin.site.register(AdminMZI, AdminMZIAdmin)
