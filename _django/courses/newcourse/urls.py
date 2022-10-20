
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.showcourses),
    path('add', views.addcourse),
    path('courses/destroy/<int:id>', views.ConfirmDestroy),
    path('destroy/<int:id>', views.destroy)

    
]
