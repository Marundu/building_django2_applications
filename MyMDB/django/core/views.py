from core.models import Movie

from django.views.generic import ListView

# class-based views

class MovieList(ListView):
    model=Movie
