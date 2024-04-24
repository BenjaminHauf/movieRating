from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Movie, Rating
from .forms import RatingForm, RegistrationForm, MovieForm
from django.shortcuts import get_object_or_404
from .recommendations import generate_recommendations
from django.db.models import Avg
# Create your views here.

@login_required
def movie_list(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movie_list') 
    else:
        form = MovieForm()

    movies = Movie.objects.filter(user=request.user)
    user_ratings = {}
    
    for movie in movies:
        rating = movie.rating_set.filter(user=request.user).first()
        user_ratings[movie.id] = rating.stars if rating else None

     # Recommendation logic
    reco_num_gpt = 3  # Number of recommended movies
    recommendations = generate_recommendations(request.user, reco_num_gpt)

    context = {
        'movies': movies,
        'user_ratings': user_ratings,
        'user': request.user,
        'recommendations': recommendations
    }

    return render(request, 'ratings/movie_list.html', context)


@login_required
def rate_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    user_rating = Rating.objects.filter(movie=movie, user=request.user).first()

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=user_rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.movie = movie
            rating.save()

            # Recalculate average rating for the movie
            avg_rating = Rating.objects.filter(movie=movie).aggregate(Avg('stars'))['stars__avg']
            movie.avg_rating = avg_rating
            movie.save()

            return redirect('movie_list')

    else:
        form = RatingForm(instance=user_rating)

    return render(request, 'ratings/rate_movie.html', {'form': form, 'movie': movie})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('movie_list')  # Redirect to the home page or any other desired page
    else:
        form = AuthenticationForm()
    return render(request, 'ratings/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'ratings/register.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return redirect('movie_list')
    return redirect('login')

