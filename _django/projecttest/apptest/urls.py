from . import views
from django.urls import path



urlpatterns=[
    path('blogs',views.fatima),
    path('',views.root),
    path('blogs-', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:val>', views.show),
    path('blogs/<int:val>/edit', views.edit),
    path('blogs/<int:val>/delete', views.destroy),
    path('blogs/json', views.lastone)


]