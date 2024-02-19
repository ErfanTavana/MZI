from django.urls import path
from . import views

urlpatterns = [
    path('ticket/', views.ticket, name='ticket_name'),
]
