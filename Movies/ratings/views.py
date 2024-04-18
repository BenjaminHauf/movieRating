from django.shortcuts import render
from django.shortcuts import redirect
from .models import Movie, Rating
from .forms import RatingForm
from django.db.models import Avg

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'ratings/movie_list.html', {'movies': movies})

   
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = Rating.objects.filter(movie=movie)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
             rating = form.save(commit=False)
             rating.user = request.user
             rating.movie_id = movie_id
             rating.save()

       
    else:
        form = RatingForm()
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'ratings/movie_detail.html', context)