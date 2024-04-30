## komplett selber hinzugefügt

from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import custom_login_view 
from .views import user_ratings

urlpatterns = [
    path('', views.user_login, name='index'),
    path('login/', views.user_login, name='index'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', custom_login_view, name='login'),  # Verwenden Sie Ihre benutzerdefinierte Anmeldeansicht
    path('user-ratings/', user_ratings, name='user_ratings'),
    path('search/', views.search_movies, name='search_movies'),
    path('submit-rating/', views.submit_rating_view, name='submit_rating'),
    path('movie-profile/', views.movie_profile, name='movie_profile'),
    path('recommend-movies/', views.recommend_movies, name='recommend_movies'),
    # path('logout/', views.custom_logout, name='logout'),

]