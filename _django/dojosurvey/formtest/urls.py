from django.urls import path
from . import views


urlpatterns=[
    path('', views.showForm),
    path('result', views.showInfo)
]