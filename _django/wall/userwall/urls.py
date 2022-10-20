
from django.urls import path
from userwall import views

from userwall.views import *
from user.views import *


urlpatterns = [

    path('welcomewall', views.welcomewall),
    path('addmessage', views.addmessage),
    path('addcomment/<int:id>', views.addcomment),
    path('delmsg', views.delmsg)


]