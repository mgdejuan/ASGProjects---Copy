from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Default Django Admin URL
    path('admin/', admin.site.urls), 
    path('', include('accounts.urls')),
    path('', include('sidebar.urls')), 
    path('dashboard/flavor/', include('dashboard.urls')),
    path('flavors/', include('dashboard.urls')),
]
