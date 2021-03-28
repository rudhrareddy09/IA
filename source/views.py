from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from django.core.mail import send_mail
import random


def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'source/home.html')


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                if request.user.councellor is not None:
                    return redirect('councellor_profile')
            except AttributeError:
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
    univ_names=UniversityName.objects.all()
    context = {
        "user_profile" : user_profile,
        "univ_records" : univ_records,
        "univ_names" : univ_names
    }
    return render(request, 'source/Profile.html', context)





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
    try:
        if request.user.councellor is not None:
            return redirect("councellor_profile")
    except AttributeError:
        return redirect('profile')


def update_univ_record(request, ur_id):
    if request.method=='POST':
        ur = get_object_or_404(UniversityRecord, pk=ur_id)
        ur.programme=request.POST["programme"]
        ur.deadline=request.POST["deadline"]
        ur.reco=request.POST.get("univ_reco_update", "") == "on"
        ur.transcripts=request.POST.get("univ_transcripts_update", "") == "on"
        ur.test=request.POST.get("univ_test_update", "") == "on"
        ur.essay=request.POST.get("univ_essay_update", "") == "on"
        ur.extra=request.POST.get("univ_extra_update", "") == "on"
        ur.info=request.POST.get("univ_info_update", "") == "on"
        ur.financial=request.POST.get("univ_financial_update", "") == "on"
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
        univ_reco= request.POST.get("univ_reco", "") == "on"
        univ_info= request.POST.get("univ_info", "") == "on"
        univ_transcripts= request.POST.get("univ_transcripts", "") == "on"
        univ_essay= request.POST.get("univ_essay", "") == "on"
        univ_financial= request.POST.get("univ_financial", "") == "on"
        univ_test= request.POST.get("univ_test", "") == "on"
        univ_extra= request.POST.get("univ_extra", "") == "on"

        ur = UniversityRecord(
            user=request.user,
            university_name=univ_name,
            programme=programme,
            deadline=deadline,
            reco=univ_reco,
            info=univ_info,
            transcripts=univ_transcripts,
            essay=univ_essay,
            financial=univ_financial,
            test=univ_test,
            extra=univ_extra,

        )
        ur.save()
        user_profile = UserProfile.objects.filter(
            user=request.user
        )
        user_profile = list(user_profile)[0]
        univ_records = UniversityRecord.objects.filter(
            user=request.user
        )
        UniversityName.objects.get_or_create(
            name=univ_name
        )


        return redirect('profile')

    return JsonResponse({
        "message" : "Only POST request supported for the URL"
    })


@login_required
def update_password(request):
    if request.method == "POST":
        current_pass = request.POST["current_password"]
        new_pass = request.POST["new_password"]
        confirm_pass = request.POST["confirm_password"]
        user = auth.authenticate(username=request.user.email, password=current_pass)
        if user is not None:
            if new_pass == confirm_pass:
                user.set_password(new_pass)
                user.save()
                auth.login(request, user)
            try:
                if request.user.councellor is not None:
                    return redirect("councellor_profile")
            except AttributeError:
                return redirect('profile')
            else:
                return JsonResponse({
                    "error" : "Passwords do not match"
                })
        else:
            return JsonResponse({
                "error" : "wrong current password"
            })

    else:
        return JsonResponse({
            "error" : "only POST request supported"
        })

def forgot_password(request):
    return render(request, "source/forgotpassword.html")

def forgot_password_form(request):
    new_password= random.randint(10000000, 99999999)
    send_mail(
        subject= "Forgot Password",
        message= f"A password reset was requested, below is your new password that can be updated after login\n new password is {new_password} ",
        from_email= "CollegeAppManager@gmail.com",
        recipient_list= [request.POST["email"]],
        fail_silently= False
    )
    user= User.objects.filter(email= request.POST["email"])
    user= list(user)[0]
    user.set_password(str(new_password))
    user.save()
    return redirect("login")

@login_required()
def essays(request):
    all_essays = Essay.objects.filter(
        user=request.user
    )
    univ_names=UniversityName.objects.all()
    context = {
        "all_essays" : all_essays,
        "univ_names": univ_names
    }
    return render(request, "source/Essays.html", context)

@login_required()
def add_essay(request):
    if request.method == "POST":
        univ_name = request.POST["univ_name"]
        prompt = request.POST["prompt"]
        content = request.POST["essay_create"]
        essay = Essay(
            user=request.user,
            univ_name=univ_name,
            prompt=prompt,
            content=content
        )
        essay.save()
        return redirect('essays')

@login_required()
def edit_essay(request, essay_id):
    if request.method == "POST":
        essay = get_object_or_404(Essay, pk=essay_id)
        univ_name = request.POST["univ_name_update"]
        prompt = request.POST["prompt_update"]
        content = request.POST["essay_update"]
        if essay is not None:
            essay.univ_name = univ_name
            essay.prompt = prompt
            essay.content = content
            essay.save()
        return redirect('essays')


def councellor_profile(request):
    user_profile = UserProfile.objects.filter(
        user = request.user
    )
    user_profile = list(user_profile)[0]
    context = {
        "user_profile" : user_profile,
    }
    return render(request, 'source/councellor_profile.html', context)


