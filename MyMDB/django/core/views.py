from core.models import Movie, Person

from django.views.generic import (
    ListView, DetailView,
)

# class-based views

class MovieDetail(DetailView):
    queryset=(
        Movie.objects.all_with_related_persons())

class MovieList(ListView):
    model=Movie
    #paginate_by=10

class PersonDetail(DetailView):
    queryset=Person.objects.all_with_prefetch_movies()
