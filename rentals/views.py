from django.shortcuts import render
from . models import Movie

# Create your views here.
from django.http import HttpResponse


def index(request):
    movies = Movie.objects.all()    
    return render(request, 'views/index.html',{'movies':movies})

def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id )
    return render(request,'views/details.html', {'movie': movie})

def movies(request):
    movies = Movie.objects.all()    
    return render(request, 'views/index.html',{'movies':movies})