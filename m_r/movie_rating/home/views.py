from django.shortcuts import render, redirect
import calendar
from datetime import datetime
from calendar import HTMLCalendar
from django.http import HttpResponseRedirect
from .models import User, Watchlist, Ratings, Recommendations
from .forms import RatingForm
from .forms import WatchlistForm
import openai
from django.contrib.auth import get_user_model
# Create your views here.


# def rating_view(request, rating_id):
#     rating = Ratings.objects.get(pk=rating_id)
#     return render(request, 'ratingView.html', {
#         'rating_view': rating
#     })

def new_rating(request):
    submitted = False
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)  # Don't save to database yet
            rating.save()  # Save the rating to generate a primary key
            # rating.user.add(request.user)  # Add the current user to the set of users associated with the rating
            return HttpResponseRedirect('/newrating?submitted=True')
    else:
        form = RatingForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'newRating.html', {'form': form, 'submitted': submitted})

def watchlist_entry(request):
    submitted = False
    if request.method == 'POST':  # the method is defined in the html file
        form = WatchlistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/watchlist_entry?submitted=True')
    else:
        form = WatchlistForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'watchlist_entry.html', {
        'form': form, 'submitted': submitted
    })

# def watchlist_entry_2(request):
#     # Assuming text_gpt is passed to the template context
#     text_gpt = "Name of the recommended movie - Explanation of why it's recommended."

#     # Split the text_gpt at the dash "-"
#     parts = text_gpt.split(" - ", 1)  # Split only at the first occurrence

#     # Assign parts to movie and description
#     if len(parts) == 2:
#         movie = parts[0]
#         desription = parts[1]
#     else:
#         movie = text_gpt
#         desription = ""

#     # Render the template with the movie and description
#     return render(request, 'watchlist_entry_2.html', {'movie': movie, 'description': desription})



def recommendations(request):
    reco_list = Recommendations.objects.all()
    return render(request, 'recommendations.html', {
        'reco_list': reco_list,})

def watchlist(request):
    watch_list = Watchlist.objects.all()
    return render(request, 'watchlist.html', {
        'watch_list': watch_list,})

def my_ratings(request):
    rating_list = Ratings.objects.all()
    return render(request, 'ratings.html', {
        'rating_list': rating_list,})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name='Django'
    month = month.capitalize()

    # convert month from string to integer

    month_number = list(calendar.month_name).index(month.capitalize())
    month_number = int(month_number)

    # create a calendar

    cal = HTMLCalendar().formatmonth(year, month_number)

    # get the current year

    now = datetime.now()
    year = now.year
    time = now.strftime('%I:%M:%S')

    return render(request, 'home.html', {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
        'time': time,
        'cal': cal,
        'year': year,
    })

def recobot(request):
    rating_list = Ratings.objects.all()
    list_movies_user = []
    list_user_rating = []
    for rating in rating_list:
        list_movies_user.append(rating.movie)
        list_user_rating.append(rating.rating)
    text_gpt = recomendation(list_movies_user, list_user_rating)
    #text_gpt = 'some text'
    
    return render(request, 'recoBot.html', {
        'text_gpt': text_gpt.replace('\n', '<br>'),  # Add text to the website ('<br>' is to html understand that need to change to a new line)
        })

# USING AI TO GET RESPONSE
def get_chatgpt_response(user_input,reco_num_gpt, completions:int):
    openai.api_key = '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 ' #'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'
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",    # choosing model of openai's AI
        prompt=user_input,                  # choosing what to use for prompting
        max_tokens=50*reco_num_gpt,                     # limit the maximum response tokens - taking 50 word for recomended movie
        temperature=1,                    # choosing temperature (more random/creative here)
        n=completions,                      # modifiable completion number
        echo=False,                         # Return the user's input in the response if set to True
        presence_penalty=1,               # higher value = more likely to introduce new topics
        frequency_penalty=0.1               # higher value = more likely to repeat information
    )
    choices = []
    for i in range(completions):
        choices.append(response.choices[i].text.strip())
    return choices

def select_movies_liked(list_movies_user,list_user_rating,movies_num):
     indices_of_5 = [i for i, x in enumerate(list_user_rating) if x == 5] # considerinf that list_user_rating are integer
     list_movies_liked = [list_movies_user[i] for i in indices_of_5]
     if len(indices_of_5) < movies_num:
        indices_of_4 = [i for i, x in enumerate(list_user_rating) if x == 4] # considerinf that list_user_rating are integer
        list_movies_liked += [list_movies_user[i] for i in indices_of_4]  
     return list_movies_liked

from .models import Recommendations

def get_already_recommended_movies():
    """Retrieve the list of movies that have already been recommended."""
    recommended_movies = Recommendations.objects.values_list('movie', flat=True)
    return recommended_movies

def recomendation(list_movies_user, list_user_rating):
    movies_num = 10             # number of movies in my list of liked movies, in this case, the top 10 (just take note 4 and 5). If movies rating 5 is bigger that 10 it just collect the rating 5, otherwise also take the movies rating 4
    reco_num_gpt = 1            # number of recommended movies from ChatGPT
    
    list_movies_liked = select_movies_liked(list_movies_user, list_user_rating, movies_num)
    already_recommended_movies = get_already_recommended_movies()
    
    # Exclude already recommended movies from the input to ChatGPT
    input_movies = [movie for movie in list_movies_liked if movie not in already_recommended_movies]
    
    try:
        # Construct the input text for GPT following the specified structure
        input_text = f"Recommend one new movie based on the movies I liked: {', '.join(input_movies)}. Do not recommend movies I've already watched or previously recommended. Answer in the format 'Title - Recommendation (about 120 words)'."
        
        # Getting the response from ChatGPT
        response = get_chatgpt_response(input_text, reco_num_gpt, 1)
        
        # Extracting movie name and recommendation from the response
        for i in range(len(response)):
            recommendation_text = response[i]
            # Checking if the recommendation text contains a "-"
            if "-" in recommendation_text:
                # Splitting the recommendation text into movie and recommendation
                movie_name, reco = recommendation_text.split(' - ')
                
                # Creating a new Recommendations instance and saving it
                recommendation_instance = Recommendations.objects.create(movie=movie_name, reco=reco)
                recommendation_instance.save()
                
                # Returning the recommendation text (if needed)
                return recommendation_text
            else:
                # If "-" is not found, make another generation automatically
                return recomendation(list_movies_user, list_user_rating)
    except Exception as e:
        text_gpt = 'Failed to communicate with Chat GPT: \n{}'.format(str(e))
        return text_gpt
