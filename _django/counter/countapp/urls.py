from django.urls import path     
from . import views



urlpatterns = [
    path('', views.showCounter),
    path('destroy', views.destroy), 
]
