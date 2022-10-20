
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allshows),
    path('new', views.newshow),
    path('create', views.createshow), 
    path('<int:id>', views.showtv),
    path('<int:id>/edit', views.editshow),
    path('<int:id>/update', views.updateshow),  
    path('<int:id>/deleteit', views.deleteshow), 
   
    

]
