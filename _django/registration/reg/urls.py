
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.regpage),
    path('reg', views.regprocess),
    path('welcome', views.welcome),
    path('login', views.log),
    path('logout', views.logout)
]