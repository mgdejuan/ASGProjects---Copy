# dashboard/views.py

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Flavor
from django.urls import reverse_lazy 
# (You may need to add: from django.shortcuts import render)

# --- C: CREATE (Add a new Flavor) ---
class FlavorCreateView(CreateView):
    model = Flavor
    fields = ['name', 'description', 'price', 'is_available']
    success_url = reverse_lazy('flavor_list')
    template_name = 'dashboard/flavor_create.html'

# --- R: READ (List All Flavors) ---
class FlavorListView(ListView):
    model = Flavor
    # 🌟 CORRECT TEMPLATE NAME 🌟
    template_name = 'dashboard/flavor_list.html' 

# --- R: READ (Detail Single Flavor) ---
class FlavorDetailView(DetailView):
    model = Flavor
    template_name = 'dashboard/flavor_detail.html' 

# --- U: UPDATE (Edit an existing Flavor) ---
class FlavorUpdateView(UpdateView):
    model = Flavor
    fields = ['name', 'description', 'price', 'is_available']
    template_name = 'dashboard/flavor_update.html'
    
    def get_success_url(self):
        return reverse_lazy('flavor_detail', kwargs={'pk': self.object.pk})

# --- D: DELETE (Remove a Flavor) ---
class FlavorDeleteView(DeleteView):
    model = Flavor
    template_name = 'dashboard/flavor_delete.html'
    success_url = reverse_lazy('flavor_list')