from django.urls import path
from . import views

urlpatterns = [
    path('admin_article/', views.admin_article, name='admin_article_name'),
]
