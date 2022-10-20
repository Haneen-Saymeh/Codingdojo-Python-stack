from django.urls import path
from . import views

urlpatterns = [
    path('', views.showForm),
    path('adddojo', views.dojo),
    path('addninja', views.ninja)
    
]