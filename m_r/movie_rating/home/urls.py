from django.urls import path, include
from . import views
from members import views as members_views

from django.contrib import admin

# path Converters
# int, str,
# slug (hyphen, underscores, etc.)
# uuid (universally unique identifier
# path (whole urls)
# custom converters

urlpatterns = [
    path('', members_views.login_user, name="login"),
    path('home', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home),
    path('myratings', views.my_ratings, name="ratings"),
    path('newrating', views.new_rating, name="new_rating"),
    path('recommendations', views.recommendations, name="recommendations"),
    path('watchlist', views.watchlist, name="watchlist"),
    path('recobot', views.recobot, name="recobot"),
    path('watchlist_entry', views.watchlist_entry, name="watchlist_entry"),
    path('rating_view', views.rating_view, name="rating_view"),
    # path('watchlist_entry_2', views.watchlist_entry_2, name="watchlist_entry_2"),
    
]
