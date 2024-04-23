from django.contrib import admin
from .models import User, Watchlist, Ratings, Recommendations

# Register your models here.

# admin.site.register(User)
# admin.site.register(Watchlist)
# admin.site.register(Ratings)
# admin.site.register(Recommendations)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('movie', 'reco', 'picture')
    search_fields = ('movie',)
    list_filter = ('movie', 'reco')
    ordering = ('movie', 'reco')
    filter_horizontal = ('user',)

@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating', 'review', 'picture')
    search_fields = ('movie', 'rating', 'review')
    list_filter = ('rating', 'review')
    ordering = ('movie', 'rating')
    filter_horizontal = ('user',)

@admin.register(Recommendations)
class RecommendationsAdmin(admin.ModelAdmin):
    list_display = ('movie', 'reco', 'description', 'picture')
    search_fields = ('movie', 'reco', 'description')
    list_filter = ('movie', 'reco')
    ordering = ('movie', 'reco')
    filter_horizontal = ('user',)