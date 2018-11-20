from core.models import Movie

from django.views.generic import (
    ListView, DetailView,
)

# class-based views

class MovieDetail(DetailView):
    model=Movie

class MovieList(ListView):
    model=Movie
