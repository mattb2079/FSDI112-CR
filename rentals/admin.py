from django.contrib import admin
from . models import Genre, Movie, Country, GenreAdmin, MovieAdmin

# Register your models here.

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Country)
