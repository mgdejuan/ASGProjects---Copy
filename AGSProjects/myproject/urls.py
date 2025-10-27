from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Default Django Admin URL
    path('admin/', admin.site.urls), 
    
    # Accounts/Authentication URLs
    path('', include('accounts.urls')),
    
    # Corrected syntax for sidebar URL
    path('sidebar/', include('sidebar.urls')), 
    
    # --- FLAVOR MANAGEMENT PATHS ---
    # 1. Existing Path (The recommended admin path)
    path('dashboard/flavor/', include('dashboard.urls')),
    
    # 2. NEW SHORTCUT PATH (To resolve the current 404 for '/flavors/')
    path('flavors/', include('dashboard.urls')),
]
