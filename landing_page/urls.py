from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('simulacao-enxame/', views.swarm_simulation, name='swarm_simulation'),
    path('telemetria-hardware/', views.hardware_dashboard, name='hardware_dashboard'),
]