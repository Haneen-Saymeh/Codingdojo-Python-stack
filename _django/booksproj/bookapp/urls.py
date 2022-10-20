from django.urls import path
from . import views



urlpatterns = [
    path('',views.showbooks), 
    path('addbook', views.addbook ),
    path('books/<int:id>', views.viewbook),
    path("authtobook/<int:id>",views.authtobook),
    path('authors', views.showauthors),
    path("addauthor", views.addauthor),
    path('authors/<int:id>', views.viewauthor),
    path('booktoauth/<int:id>', views.booktoauth)
    
]
