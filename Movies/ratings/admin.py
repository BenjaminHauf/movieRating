from django.contrib import admin
from .models import Movie
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year')
    search_fields = ('title', 'genre', 'release_year')

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

admin.site.register(Movie, MovieAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)  # Register the CustomUserAdmin instead