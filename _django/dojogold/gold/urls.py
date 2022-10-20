from django.urls import path
from . import views

urlpatterns = [
    path('', views.startgame),
    path('process', views.process),
    path('destroy', views.reset)
]