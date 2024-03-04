from django.contrib import admin
from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description', 'image')
    list_filter = ('categories', 'tags')
    search_fields = ('title', 'description')
    filter_horizontal = ('categories', 'tags')


admin.site.register(Portfolio, PortfolioAdmin)
