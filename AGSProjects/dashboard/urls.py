from django.urls import path
from . import views

urlpatterns = [
    path('flavors/', views.flavor_list, name='flavor_list'),
]
