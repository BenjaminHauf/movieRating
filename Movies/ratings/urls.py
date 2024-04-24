from django.urls import path
from django.contrib.auth import views as auth_views
from .views import movie_list, register, rate_movie, login_view, logout_view

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('rate_movie/<int:movie_id>/', rate_movie, name='rate_movie'),
]