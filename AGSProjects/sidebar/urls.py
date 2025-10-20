from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('notifications/', views.notifications, name='notifications'),
    path('log-history/', views.log_history, name='log_history'),
    path('about/', views.about, name='about'),
]
