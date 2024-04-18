from django.contrib import admin
from movies.models import *

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = (
        'role',
        'name',
    )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'rating',
        'title',
        'id',
    )

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'likes',
        'movie',
    )