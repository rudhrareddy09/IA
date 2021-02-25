from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'source/home.html')


def about(request):
    return render(request, 'source/about.html')

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
    else:
        return render(request, 'source/login.html')

"""
TODO
"""
def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    return render(request, 'source/signup.html')


def add_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        password_repeat = request.POST["password-repeat"]
        if password == password_repeat:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            auth.login(request, user)
            return redirect('home')
    else:
        return redirect('signup')

@login_required
def profile(request):
    return render(request, 'source/Profile.html')



"""
1) Ready all htmls (make sure that each one can be accessed in a standalone manner from the browser)
2) Connect all necessary htmls to the navbar
3) Place all images in ia1/static/images
4) Ready the Profile Page 
5) Place all the CSS assets in ia1/static/assets
6) Make sure bootstrap, jquery are added in all htmls
"""



