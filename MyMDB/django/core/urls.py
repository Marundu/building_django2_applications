from django.urls import path

from . import views

app_name='core'

urlpatterns=[
    path('movies',
        views.MovieList.as_view(),
        name='MovieList'),
    
    path('movies/<int:pk>',
        views.MovieDetail.as_view(),
        name='MovieDetail'),
    ]
