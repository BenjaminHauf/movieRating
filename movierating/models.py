from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators   import MinValueValidator, MaxValueValidator

# Create your models here.
class actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class genre(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class regie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class movie(models.Model):
    id = models.AutoField(primary_key=True)
    regieID = models.ForeignKey(regie, on_delete=models.CASCADE)
    genre = models.ForeignKey(genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    releaseDate = models.DateTimeField()
    def __str__(self):
        return self.title

class movieActor(models.Model):
    id = models.AutoField(primary_key=True)
    ActorsID = models.ForeignKey(actor, on_delete=models.CASCADE)
    MovieID = models.ForeignKey(movie, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ActorsID.name} - {self.MovieID.title} stars"
    
class rating(models.Model):
    id = models.AutoField(primary_key=True)
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movieID = models.ForeignKey(movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"{self.title} - {self.movieID} -{self.userID} stars"