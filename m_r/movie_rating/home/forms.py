from django import forms
from django.forms import ModelForm
from .models import User, Watchlist, Ratings, Recommendations



class WatchlistForm(ModelForm):
    class Meta:
        model = Watchlist
        fields = ['movie', 'reco', 'desription']
        labels = {
            'movie': '',
            'reco': '',
            'desription': '',
        }
        widgets = {
            'movie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie Name'}),
            'reco': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Recommendation'}),
            'desription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

    
class RatingForm(ModelForm):
    class Meta:
        model = Ratings
        fields = ['movie', 'rating', 'review']
        labels = {
            'movie': '',
            'rating': '',
            'review': '',
         
        }
        widgets = {
            'movie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie Name'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating', 'min': 1, 'max': 5}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Review'}),
        }
