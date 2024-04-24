from django import forms
from django.forms import ModelForm
from .models import User, Watchlist, Ratings, Recommendations



class WatchlistForm(ModelForm):
    class Meta:
        model = Watchlist
        fields = ['movie', 'user']
        labels = {
            'movie': '',
            'user': '',
        }
        widgets = {
            'movie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie Name'}),
            'user': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'User'}),
        }
    
class RatingForm(ModelForm):
    class Meta:
        model = Ratings
        fields = ['movie', 'rating', 'review', 'picture', 'user']
        labels = {
            'movie': '',
            'rating': '',
            'review': '',
            'picture': '',
            'user': '',
        }
        widgets = {
            'movie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie Name'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Review'}),
            'picture': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Picture URL'}),
            'user': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'User'}),
        }