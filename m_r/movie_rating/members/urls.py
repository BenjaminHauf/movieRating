from .views import register_user    
from django.urls import path    # Import the path function
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),   # The home page
    path('login', views.login_user, name='login'),  # The login page
    path('logout', views.logout_user, name='logout'),   # The logout page
    path('register', views.register_user, name='register'),     # The register page

]
