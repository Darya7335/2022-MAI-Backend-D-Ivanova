from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from Movies.models import Movie, Director, Country

@require_http_methods(["GET", "POST"])

def movie_index(request):
    return HttpResponse('Welcome to my website! Here you will learn a lot of interesting things about movies.')

def all_directors(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        return JsonResponse({
            'Directors': list(directors.values())
        })

def all_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        return JsonResponse({
            'Movies': list(movies.values())
        })

def all_countries(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        return JsonResponse({
            'Countries': list(countries.values())
        })

def all_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        return JsonResponse({
            'Movies': list(movies.values())
        })

def find_movies(request):
    movie = request.GET.get("m", None)
    try:
            f_movie = Movie.objects.get(title=movie)
            f_country = Country.objects.get(id=f_movie.CountryID_id)
            f_dir = Director.objects.get(id=f_movie.DirectorID_id)
            return JsonResponse({"Title": f_movie.title, "Year": f_movie.year, "Counry": f_country.CountryName, "Director": f_dir.DirectorName})
    except Movie.DoesNotExist:
            return JsonResponse({"status": False, "msg": "ERROR"})

def find_by_director(request):
    director = request.GET.get("d", None)
    try:
            f_director = Director.objects.get(DirectorName = director)
            f_movie = Movie.objects.filter(DirectorID_id=f_director.id)
            return JsonResponse({
                    'Movies': list(f_movie.values())
                })
    except Movie.DoesNotExist:
            return JsonResponse({"status": False, "msg": "ERROR"})

def find_by_year(request):
    date = request.GET.get("y", None)
    try:
            f_movie = Movie.objects.filter(year=date)
            return JsonResponse({
                    'Movies': list(f_movie.values())
                })
    except Movie.DoesNotExist:
            return JsonResponse({"status": False, "msg": "ERROR"})

@csrf_exempt 

def add_director(request):
    if request.method == 'GET':
        return JsonResponse({"status": False, "msg": "Поменяйте GET на POST"})

    if request.method == 'POST':
        name = request.GET.get("DirectorName", None)
        if not name:
            return JsonResponse({"status": False, "msg": "Укажите имя режисёра"})

        duplicates = Director.objects.filter(DirectorName=name)
        if len(duplicates) > 0:
            return JsonResponse({"status": False, "msg": "Коллизия, попробуйте добавить другого режисёра"})
            
        new_director = Director()
        new_director.DirectorName = name
        new_director.save()
        
        return JsonResponse({"status": True, "msg": "Режисёр добавлен"})

@csrf_exempt 
def add_country(request):
    if request.method == 'GET':
        return JsonResponse({"status": False, "msg": "Поменяйте GET на POST"})

    if request.method == 'POST':
        country = request.GET.get("CountryName", None)
        if not country:
            return JsonResponse({"status": False, "msg": "Укажите страну"})

        duplicates = Country.objects.filter(CountryName=country)
        if len(duplicates) > 0:
            return JsonResponse({"status": False, "msg": "Коллизия, попробуйте добавить другую страну"})
            
        new_country = Country()
        new_country.CountryName = country
        new_country.save()
        
        return JsonResponse({"status": True, "msg": "Страна добавлена"})

@csrf_exempt 
def add_movie(request):
    if request.method == 'GET':
        return JsonResponse({"status": False, "msg": "Поменяйте GET на POST"})

    if request.method == 'POST':
        title = request.GET.get("t", None)
        year = request.GET.get("y", None)
        #countryid = request.GET.get("c", None)
        countryname = request.GET.get("c", None)
        #directorid = request.GET.get("d", None)
        directorname = request.GET.get("d", None)
        if not title:
            return JsonResponse({"status": False, "msg": "Укажите название фильма"})

        duplicates = Movie.objects.filter(title=title)
        if len(duplicates) > 0:
            return JsonResponse({"status": False, "msg": "Коллизия, попробуйте добавить другой фильм"})
            

        try:
            f_country = Country.objects.get(CountryName=countryname)
        
        except:
            new_country = Country()
            new_country.CountryName = countryname
            new_country.save()
                
        try:
            f_director = Director.objects.get(DirectorName=directorname)

        except:
            new_director = Director()
            new_director.DirectorName = directorname
            new_director.save()

        f_country = Country.objects.get(CountryName=countryname)
        f_director = Director.objects.get(DirectorName=directorname)
        new_movie = Movie()
        new_movie.title = title
        new_movie.year = year
        new_movie.CountryID_id = f_country.id
        new_movie.DirectorID_id = f_director.id
        new_movie.save()

        

        
        return JsonResponse({"status": True, "msg": "Фильм добавлен"})

# Заглушка из 3 лабы

def movie_page(request):
    if request.method == "GET":
        name = request.GET.get("name", "Трасса 60")
        year = request.GET.get("year", "2001")
        return JsonResponse({"name": name, "year": year})
    elif request.method == "POST":
        name = request.GET.get("name", "Круелла")
        year = request.GET.get("year", "2021")
        return JsonResponse({"name": name, "year": year, "status": "OK"})
