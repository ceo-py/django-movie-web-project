from django.shortcuts import render
from .models import Movie


# Create your views here.

def index(request):
    return render(request, 'catalog/index.html')


def movie_detail(request):
    # movie = Movie.objects.get(id=movie_id)
    return render(request, 'catalog/movie_details.html')

