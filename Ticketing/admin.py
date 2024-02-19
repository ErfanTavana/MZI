from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'user_type', 'priority', 'phone_number', 'email', 'created_at']
    search_fields = ['name', 'subject', 'user_type', 'priority', 'phone_number', 'email', 'additional_description']
    list_filter = ['user_type', 'priority', 'created_at']


admin.site.register(Ticket, TicketAdmin)
