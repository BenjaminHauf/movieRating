

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import rating, movie, genre, regie
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from openai import OpenAI
from datetime import datetime

def convert_to_datetime(date_string):
    print(date_string)
    date_object = datetime.strptime(date_string.strip(), '%B %d, %Y')
    django_formatted_date = date_object.strftime('%Y-%m-%d %H:%M:%S')
    return django_formatted_date


    
def chatgptquester(statement):
    api_key = ''
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": statement},
    ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def userMovieempfehlung(goodmovies, badmovies):
    if len(goodmovies) <5 and len(badmovies) < 2:
        print(goodmovies)
        return "not enough movies" 
    print(goodmovies)       
    chatgptAsk = "Give me 5 movie recommendations. I liked the following movies:"
    for element in goodmovies:
        chatgptAsk = chatgptAsk + element
        print(element)
    print(chatgptAsk)
    chatgptAsk = chatgptAsk + "and I disliked the following movies:"
    for element in badmovies:
        chatgptAsk = chatgptAsk + element
    print(chatgptAsk)
    return chatgptquester(chatgptAsk)

def FindMovie(searchMovie):
    question = "Give me the following information about the movie " + searchMovie + " Title, Genre, Description, Director, Release Date, Cast (only the name of the cast)"
    answer = chatgptquester(question)


    NumberListForMessagesList = [6, 6, 12, 9, 13, 5]

    messagesList = [answer.find("Title:"),
                    answer.find("Genre:"),
                    answer.find("Description:"),
                    answer.find("Director:"),
                    answer.find("Release Date:"),
                    answer.find("Cast:") ]

    messagesListB = []

    counter = 0
    for element in messagesList:
        #print(element)
        counter = counter +1
        if counter < len(messagesList):
            messagesListB.append(answer[element+NumberListForMessagesList[counter-1]: messagesList[counter]])
        else:
            messagesListB.append(answer[element+NumberListForMessagesList[counter-1]:])

    # for element in messagesListB:
    #     #print(element.strip())
    castList = messagesListB[-1].split(",")
    return messagesListB + castList




def user_login(request):
    if request.method == 'POST':
            print("Ich wurde als REQUEST Methode erkannt")
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            print("Ich wurde zur Datenbankabfrage")
            if user is not None:
                print("Ich wurde gefunden")
                login(request, user)
                return redirect('user_ratings')
            else: 
                  print("ich wurde nicht gefunden")
                  return render(request, 'login.html', {'error': 'Ungültige Anmeldeinformationen'})
    return render(request, 'movierating/index.html', {})

def custom_login_view(request):
    
    return render(request, 'movierating/custom_login.html', {})  

def user_ratings(request):
    user_ratings = rating.objects.filter(userID=request.user)  
    return render(request, 'movierating/custom_ratings.html', {'user_ratings': user_ratings})


def search_movies(request):
    query = request.GET.get('q')
    print("ich bin in der search movie")
    try: 
            movie_obj = movie.objects.get(title=query)
            print("Ich erfolgreich das Object erstellt")
    except movie.DoesNotExist:
            print("movie wurde nicht gefunden")
            if "yes" in chatgptquester("Is '"+ query + "' a movie? If you don't know the movie, answer with No. Answer only yes or no. If the name of the movie is not spelled correctly, answer “No.” If the film title is not complete, answer no").lower():
                print("yes")
                DataListMovie = FindMovie(query)
                genre1 = DataListMovie[1]
                regie1 = DataListMovie[3]
                genre_obj, _ = genre.objects.get_or_create(name=genre1)                 
                regie_obj, _ = regie.objects.get_or_create(name=regie1)

                # genre_obj = genre.objects.get(name = genre1)
                # regie_obj = regie.objects.get(name = regie1)
                newMovie = movie.objects.create(
                regieID = regie_obj,
                genre = genre_obj,
                title = DataListMovie[0],
                text = DataListMovie[2],
                releaseDate = convert_to_datetime(DataListMovie[4],                                )     
                )
                newMovie.save()  
    if query:
        movies = movie.objects.filter(title__icontains=query)
    else:
        movies = movie.objects.all()
    return render(request, 'movierating/all_movie.html', {'movies': movies})

def rating_quest(value, valueURL):
    request = value
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')  

        try: 
            movie_obj = movie.objects.get(id=movie_id)
        except movie.DoesNotExist:
            return HttpResponse("Ungültige Movie ID!")

 
        try:
            old_rating = rating.objects.get(userID=request.user, movieID=movie_obj)
            old_rating.title = request.POST.get('title')
            old_rating.text = request.POST.get('text')
            old_rating.rating = int(request.POST.get('rating'))
            old_rating.created_date = timezone.now()
            old_rating.published_date = None
            old_rating.save()
            return HttpResponse("Bewertung erfolgreich aktualisiert!")
        except rating.DoesNotExist:
            rating_value = request.POST.get('rating')
            if rating_value.isdigit() and 0 <= int(rating_value) <= 5:
                ratingvalue = int(rating_value)
                new_rating = rating.objects.create(
                    userID=request.user,
                    movieID=movie_obj,
                    title=request.POST.get('title'),
                    text=request.POST.get('text'),
                    rating=ratingvalue,
                    created_date=timezone.now(),
                    published_date=None  
                )
                new_rating.save()
                return HttpResponse("Bewertung erfolgreich eingereicht!")
            else:
                return HttpResponse("Ungültiges Rating!")

    else:
        return HttpResponse("Nur POST-Anfragen sind erlaubt!")


def submit_rating_view(request):
    if request.method == 'POST':

        movie_id = request.POST.get('movie_id')  
        try: 
            movie_obj = movie.objects.get(id=movie_id)
        except movie.DoesNotExist:
            return HttpResponse("Ungültige Movie ID!")

        try:
            old_rating = rating.objects.get(userID=request.user, movieID=movie_obj)
            old_rating.title = request.POST.get('title')
            old_rating.text = request.POST.get('text')
            old_rating.rating = int(request.POST.get('rating'))
            old_rating.created_date = timezone.now()
            old_rating.published_date = None
            old_rating.save()
            return HttpResponse("Bewertung erfolgreich aktualisiert!")
        except rating.DoesNotExist:

            rating_value = request.POST.get('rating')
            if rating_value.isdigit() and 0 <= int(rating_value) <= 5:
                ratingvalue = int(rating_value)

                new_rating = rating.objects.create(
                    userID=request.user,
                    movieID=movie_obj,
                    title=request.POST.get('title'),
                    text=request.POST.get('text'),
                    rating=ratingvalue,
                    created_date=timezone.now(),
                    published_date=None  
                )
                new_rating.save()
                return HttpResponse("Bewertung erfolgreich eingereicht!")
            else:
                return HttpResponse("Ungültiges Rating!")

    else:
        return HttpResponse("Nur POST-Anfragen sind erlaubt!")
        
         
def movie_profile(request):

    movie_id = request.GET.get('movie_id')
    
    if movie_id:
        
        return loadMovieProfil(request, movie_id)
    else:
        return HttpResponse("Movie ID not provided")

def loadMovieProfil(request, movie_id):

    movie_object = get_object_or_404(movie, id=movie_id)
    

    ratings = rating.objects.filter(movieID=movie_object)
    

    context = {
        'movie': movie_object,
        'ratings': ratings
    }
    
    if request.method == 'POST':
        return rating_quest(request, 1)

 
    return render(request, 'movierating/movie_profile.html', context)

def recommend_movies(request):

    good_ratings = rating.objects.filter(userID=request.user, rating__gte=4)[:10]  
    bad_ratings = rating.objects.filter(userID=request.user, rating__lte=2)[:5]  

    good_movies = [rating.movieID.title for rating in good_ratings]
    bad_movies = [rating.movieID.title for rating in bad_ratings]

    recommendations = userMovieempfehlung(good_movies, bad_movies)

    return render(request, 'movierating/recommendations.html', {'recommendations': recommendations})

# def custom_logout(request):
#     logout(request)
#     return redirect('index')
