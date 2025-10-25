# dashboard/admin.py

from django.contrib import admin
from .models import Flavor

# Option 1: Simple registration
# admin.site.register(Flavor) 

# Option 2: Enhanced registration for better admin visibility (Recommended)
@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    # What fields to show on the change list page (the list of all flavors)
    list_display = ('name', 'price', 'is_available', 'created_at')
    
    # Add a search box based on these fields
    search_fields = ('name', 'description')
    
    # Add filters to the sidebar
    list_filter = ('is_available', 'created_at')