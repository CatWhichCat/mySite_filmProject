from django.shortcuts import render
from django.views import View

from .models import *
# Create your views here.

class MovieView(View):
    '''Список фильмов'''
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movie_list.html", {'movie_list': movies})