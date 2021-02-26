"""ia1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from source import views as sviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sviews.home, name="home"),
    path('about', sviews.about, name='about'),
    path('login', sviews.login , name='login'),
    path('signup', sviews.signup , name='signup'),
    path('add_user', sviews.add_user, name='add_user'),
    path('profile', sviews.profile, name='profile'),
    path('resources', sviews.resources, name='resources'),
    path('logout', sviews.logout),
]
