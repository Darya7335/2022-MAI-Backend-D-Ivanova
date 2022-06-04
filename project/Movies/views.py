from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["GET", "POST"])

def movie_index(request):
    return HttpResponse('Welcome to my website! Here you will learn a lot of interesting things about movies.')

@csrf_exempt 
def movie_page(request):
    if request.method == "GET":
        name = request.GET.get("name", "Interstate 60")
        year = request.GET.get("year", "2001")
        return JsonResponse({"name": name, "year": year})
    elif request.method == "POST":
        name = request.GET.get("name", "Cruella")
        year = request.GET.get("year", "2021")
        return JsonResponse({"name": name, "year": year, "status": "OK"})
