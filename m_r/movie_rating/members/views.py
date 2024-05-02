from django.shortcuts import render, redirect   # render is to render the html file, redirect is to redirect to another page
from django.contrib.auth import login, authenticate, logout   # Import the login, authenticate, and logout functions
from django.contrib import messages     # Import the messages module
from django.contrib.auth.forms import UserCreationForm      # Import the UserCreationForm

def login_user(request):
    if request.method == 'POST':    # If the form is submitted
        username = request.POST['username'] # Get the username from the form
        password = request.POST['password'] # Get the password from the form
        user = authenticate(request, username=username, password=password)  # Authenticate the user
        if user is not None:    # If the user is authenticated
            login(request, user)    # Log the user in
            messages.success(request, f'Hi {user.username}, you have successfully logged in')   # Display a success message
            return redirect('home') # Redirect to the home page
        else:
            messages.error(request, 'Invalid username or password')     # Display an error message
            return redirect('login')        # Redirect to the login page
    return render(request, 'registration/login.html', {})       # Render the login page

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)   # Create a form object with the data from the POST request
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')    # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})    # Render the registration page with the form
