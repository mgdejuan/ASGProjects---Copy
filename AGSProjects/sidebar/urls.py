from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('flavors/', views.flavors, name='flavors'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('toppings/', views.toppings, name='toppings'),
    path('packaging/', views.packaging, name='packaging'),
    path('inventory/', views.inventory, name='inventory'),
    path('notifications/', views.notifications, name='notifications'),
    path('log-history/', views.log_history, name='log_history'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_view, name='logout'),
]
