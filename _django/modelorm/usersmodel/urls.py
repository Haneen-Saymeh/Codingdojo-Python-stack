from django.urls import path
from . import views

urlpatterns = [
    path('', views.regForm),
    path('handle', views.handle),
    path('show', views.showForm)
    
]

