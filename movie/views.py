from django.shortcuts import render
from .api import *

def Home(request):

    return render(request, 'HomeScreen.html')

def Discover(request):
    return render(request, 'DiscoverScreen.html')

def MovieDetails(request, movie_id):
    context = movie_details(request, movie_id)  # Call the movie_details function with the movie_id
    return render(request, 'MovieDetails.html', context)
    