from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies',views.movies, name='movies_movies'),
    path('<int:movie_id>',views.details, name='movies_detail'),
]