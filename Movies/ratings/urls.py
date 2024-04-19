from django.urls import path
from . import views
from .views import login_view, register

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
]