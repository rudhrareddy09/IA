from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UniversityRecord
from django.http import JsonResponse

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
        name = request.POST["name"]
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
            user_profile = UserProfile(
                user=user,
                name=name
            )
            user_profile.save()
            return redirect('home')
    else:
        return redirect('signup')

@login_required
def profile(request):
    user_profile = UserProfile.objects.filter(
        user = request.user
    )
    user_profile = list(user_profile)[0]
    univ_records = UniversityRecord.objects.filter(
        user=request.user
    )
    context = {
        "user_profile" : user_profile,
        "univ_records" : univ_records
    }
    return render(request, 'source/Profile.html', context)


def resources(request):
    return render(request, 'source/resources.html')

"""
1) Ready all htmls (make sure that each one can be accessed in a standalone manner from the browser)
2) Connect all necessary htmls to the navbar
3) Place all images in ia1/static/images
4) Ready the Profile Page 
5) Place all the CSS assets in ia1/static/assets
6) Make sure bootstrap, jquery are added in all htmls
"""


"""
git status (tells you which files have been changed)
git add . (adds ALL files to the staging area)
git commit -m "enter your commit message"
git push origin main
"""


def update_dp(request):
    user_profile = UserProfile.objects.filter(
        user = request.user
    )
    user_profile = list(user_profile)[0]
    user_profile.profile_pic = request.FILES['dp_new']
    user_profile.save()

    univ_records = UniversityRecord.objects.filter(
        user=request.user
    )
    context = {
        "user_profile" : user_profile,
        "univ_records" : univ_records
    }
    return redirect('profile')


def update_univ_record(request, ur_id):
    if request.method=='POST':
        ur = get_object_or_404(UniversityRecord, pk=ur_id)
        ur.programme=request.POST["programme"]
        ur.deadline=request.POST["deadline"]
        ur.save()
        return redirect('profile')
    return JsonResponse({
        "message" : "Only POST request supported for the URL"
    })


def add_univ_record(request):
    if request.method=='POST':
        univ_name = request.POST["univ_name"]
        programme = request.POST["programme"]
        deadline = request.POST["deadline"]
        ur = UniversityRecord(
            user=request.user,
            university_name=univ_name,
            programme=programme,
            deadline=deadline
        )
        ur.save()
        user_profile = UserProfile.objects.filter(
            user=request.user
        )
        user_profile = list(user_profile)[0]
        univ_records = UniversityRecord.objects.filter(
            user=request.user
        )
        context = {
            "user_profile": user_profile,
            "univ_records": univ_records
        }
        return redirect('profile')

    return JsonResponse({
        "message" : "Only POST request supported for the URL"
    })



