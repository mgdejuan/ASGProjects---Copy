from django.shortcuts import render
from .models import Flavor

def flavor_list(request):
    flavors = Flavor.objects.all()
    return render(request, 'dashboard/flavors.html', {'flavors': flavors})
