from django import forms
from .models import Rating, Movie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_year']