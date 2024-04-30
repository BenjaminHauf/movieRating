from django.contrib import admin
from .models import actor, genre, regie, movie, movieActor
# Register your models here.
from django.contrib import admin
# from .models import rating

# admin.site.register(rating)

admin.site.register(actor)
admin.site.register(genre)
admin.site.register(regie)
admin.site.register(movie)
admin.site.register(movieActor)