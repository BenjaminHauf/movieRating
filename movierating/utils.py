from .models import Genre, Regie, Movie
from datetime import datetime

def add_movies():
    # Annahme: Sie haben bereits Autoren, Regisseure und Genres in Ihrer Datenbank

    # Erstellen Sie Instanzen für den Film
    regie = Regie.objects.get(name="Jane Doe")    # Beispielregisseurname
    genre = Genre.objects.get(name="Action")      # Beispielgenrename

    movie1 = Movie(
        regieID=regie,
        genre=genre,
        title="Movie Title 1",
        text="Description of Movie 1",
        releaseDate=datetime.now()
    )
    movie1.save()

    movie2 = Movie(
        regieID=regie,
        genre=genre,
        title="Movie Title 2",
        text="Description of Movie 2",
        releaseDate=datetime.now()
    )
    movie2.save()