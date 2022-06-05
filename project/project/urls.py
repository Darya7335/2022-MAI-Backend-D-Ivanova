from django.contrib import admin
from django.urls import path
from Movies.views import movie_index, movie_page, all_directors, add_director, all_countries, add_country, all_movies, add_movie, find_movies, find_by_director, find_by_year
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_index, name='home'),
    path('index', movie_index, name='home'),   
    path('movie', movie_page, name='movie'), 
    path('directors', all_directors, name='Режисёры'),
    path('add-d', add_director, name='Добавление режисёра'),
    path('countries', all_countries, name='Страны'),
    path('add-с', add_country, name='Добавление страны'),
    path('movies', all_movies, name='Фильмы'),
    path('add-m', add_movie, name='Добавление фильма'),
    path('find-movie', find_movies, name='Поиск фильма'),
    path('find-by-director', find_by_director, name='Поиск по режисёру'),
    path('find-by-year', find_by_year, name='Поиск по году'),
]
