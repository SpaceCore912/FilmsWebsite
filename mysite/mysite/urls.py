"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.views.generic.base import TemplateView,RedirectView
from polls.views import ProfileView
from django.urls import reverse
from dotenv import load_dotenv
load_dotenv()
import os

urlpatterns = [
    path("", include("polls.urls")),
    path(os.environ.get("UUID"), admin.site.urls),
    path("accounts/",include("django.contrib.auth.urls")),
    path("profile/<user_username>",RedirectView.as_view(pattern_name="polls:profile"),name="profile"),

    path("register/",TemplateView.as_view(template_name="polls/home.html"),name="home"),

    path("accounts/", include("accounts.urls")),

]
