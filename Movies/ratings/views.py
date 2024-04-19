from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import Movie, Rating
from .forms import RatingForm, RegistrationForm
from django.db.models import Avg

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'ratings/movie_list.html', {'movies': movies})

   
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    rating = Rating.objects.filter(movie=movie)
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('movie_list')  # Redirect to the home page or any other desired page
    else:
        form = AuthenticationForm()
    return render(request, 'ratings/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'ratings/register.html', {'form': form})