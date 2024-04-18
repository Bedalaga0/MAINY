from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'movies/home.html') 

def movie_detail(request, movie_id):
    return render(request, 'movies/detail/movie_detail.html')

def composer_detail(request, composer_id):
    return render(request, 'movies/detail/composer_detail.html')

def genre_detail(request, genre_id):
    return render(request, 'movies/detail/genre_detail.html')

def actor_detail(request, actor_id):
    return render(request, 'movies/detail/actor_detail.html')

def director_detail(request, director_id):
    return render(request, 'movies/detail/director_detail.html')

def directors_list(request):
    return render(request, 'movies/list/directors_list.html')

def actors_list(request):
    return render(request, 'movies/list/actors_list.html')

def genres_list(request):
    return render(request, 'movies/list/genres_list.html')

def composers_list(request):
    return render(request, 'movies/list/composers_list.html')

def movies_list(request):
    return render(request, 'movies/list/movies_list.html')