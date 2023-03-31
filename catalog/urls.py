from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movie_detail, name='movie_detail')
]