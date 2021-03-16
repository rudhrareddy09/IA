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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sviews.home, name="home"),
    path('about', sviews.about, name='about'),
    path('login', sviews.login , name='login'),
    path('signup', sviews.signup , name='signup'),
    path('add_user', sviews.add_user, name='add_user'),
    path('profile', sviews.profile, name='profile'),
    path('resources', sviews.resources, name='resources'),
    path('logout', sviews.logout, name="logout"),
    path('update_dp', sviews.update_dp, name="update_dp"),
    path('update_univ_record/<int:ur_id>', sviews.update_univ_record, name="update_univ_record"),
    path('add_univ_record', sviews.add_univ_record, name="add_univ_record"),
    path('update_password', sviews.update_password, name="update_password"),
    path('forgot_password', sviews.forgot_password, name="forgot_password"),
    path('forgot_password_form', sviews.forgot_password_form, name="forgot_password_form"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

