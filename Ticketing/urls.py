from django.urls import path
from . import views

urlpatterns = [
    path('ticket/', views.ticket, name='ticket_name'),
    path('admin_ticket/', views.admin_ticket, name='admin_ticket_name'),

]
