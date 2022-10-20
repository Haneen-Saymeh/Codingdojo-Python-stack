from django.urls import path
from . import views
urlpatterns = [
    path('', views.pick),
    path('process', views.process),
    path('destroy', views.destroy)
]