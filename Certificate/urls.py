from django.urls import path
from . import views

urlpatterns = [
    path('admin_certificate/', views.admin_certificate, name='admin_certificate_name'),
    path('certificate/', views.certificate, name='certificate_name'),
]

