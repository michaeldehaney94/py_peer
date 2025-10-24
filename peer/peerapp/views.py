from datetime import datetime
# Import the User model to store new user
from django.contrib.auth.models import User, auth
# used to send a message to UI if failure occurs
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')


# sign up page
def signup(request):
    current_year = datetime.now().year

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # check the user table to see if email already exists
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken!')
                return redirect('signup')
            # check user table if username already exists
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken!')
                return redirect('signup')
            else:
                # if email and username do not exist in the user table, save data
                user = User.objects.create_user(username=username, email=email, password=password)
                # create and save new user
                user.save()

                # automatically log user in

                # create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                # save new profile
                new_profile.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Does Not Match!')
            # redirect to the sign-up page to try again
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'year': current_year})


# sign-in page
def signin(request):
    return render(request, 'signin.htmlgit')