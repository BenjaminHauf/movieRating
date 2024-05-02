from django import forms    # Import the forms module
from django.forms import ModelForm  # Import the ModelForm class
from .models import User, Watchlist, Ratings, Recommendations   # Import the User, Watchlist, Ratings, and Recommendations models



class WatchlistForm(ModelForm):    # The WatchlistForm class
    class Meta:    # The Meta class
        model = Watchlist   # The Watchlist model
        fields = ['movie', 'reco', 'desription']    # The fields to include in the form
        labels = {  # The labels for the fields
            'movie': '',
            'reco': '',
            'desription': '',
        }
        widgets = { # The widgets for the fields
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
