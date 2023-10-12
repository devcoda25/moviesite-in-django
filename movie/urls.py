from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.Home, name="index"),
    path('discover',views.Discover, name="discover"),
    path('movie/<int:movie_id>/',views.MovieDetails, name='movie_view'),
]
    
