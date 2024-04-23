from django.urls import path
from . import views

# path Converters
# int, str,
# slug (hyphen, underscores, etc.)
# uuid (universally unique identifier
# path (whole urls)
# custom converters

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home),
    path('myratings', views.my_ratings, name="ratings"),
    path('newrating', views.new_rating, name="new_rating"),
    # path('rating_view/<rating_id>', views.rating_view, name="rating_view"),
]
