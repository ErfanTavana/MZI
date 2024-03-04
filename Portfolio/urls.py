from django.urls import path
from . import views

urlpatterns = [
    path('admin_portfolio/', views.admin_portfolio, name='admin_portfolio_name'),
]
