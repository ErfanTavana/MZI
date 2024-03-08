from django.urls import path
from . import views

urlpatterns = [
    path('admin_portfolio/', views.admin_portfolio, name='admin_portfolio_name'),
    path('portfolio/', views.portfolio, name='portfolio_name'),

]
