from django.shortcuts import render
import calendar
from datetime import datetime
from calendar import HTMLCalendar
from django.http import HttpResponseRedirect
from .models import User, Watchlist, Ratings, Recommendations
from .forms import RatingForm
# Create your views here.





# def rating_view(request, rating_id):
#     rating = Ratings.objects.get(pk=rating_id)
#     return render(request, 'rating_view.html', {
#         'rating': rating
#     })

def new_rating(request):
    submitted = False
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newrating?submitted=True')
    else:
        form = RatingForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'newRating.html', {
        'form': form, 'submitted': submitted
    })

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