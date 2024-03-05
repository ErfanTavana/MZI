from django.contrib import admin
from .models import Certificate

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    search_fields = ('title', 'user__username')

admin.site.register(Certificate, CertificateAdmin)
