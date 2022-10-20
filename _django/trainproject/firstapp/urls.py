from django.urls import path     
# from . import views
import firstapp.views as view
urlpatterns = [
    path("", view.root)
]
