from django.db import models    # Import the models module
from django.contrib.auth.models import User   # Import the User model

# Create your models here.


class User(models.Model):   
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Watchlist(models.Model):  # The Watchlist model
    movie = models.CharField(max_length=120)        # The name of the movie
    reco = models.TextField(blank=True, null=True)      # The recommendation
    desription = models.TextField(blank=True, null=True)    # The description
    picture = models.URLField(blank=True, null=True)    # The picture of the movie
    user = models.ManyToManyField('User')   # The user who added the movie to the watchlist

    def __str__(self):  # The string representation of the model
        return self.movie   # Return the name of the movie
    
class Ratings(models.Model):
    movie = models.CharField(max_length=120)
    rating = models.IntegerField()
    review = models.TextField(blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.movie
    
class Recommendations(models.Model):
    movie = models.CharField(max_length=120)
    reco = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    user = models.ManyToManyField('User',)

    def __str__(self):
        return self.movie
    
