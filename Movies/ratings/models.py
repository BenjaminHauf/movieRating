from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='Unknown')
    release_year = models.IntegerField()

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(
            validators=[MinValueValidator(1), MaxValueValidator(5)],default=1
    )


    def __str__(self):
        return f"{self.movie.title} - {self.rating} stars"