from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return render(request, 'landing_page/index.html')

def swarm_simulation(request):
    return render(request, 'landing_page/swarm_simulation.html')

def hardware_dashboard(request):
    return render(request, 'landing_page/hardware_dashboard.html')