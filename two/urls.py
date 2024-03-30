from django.urls import path
from django.shortcuts import render

from . import views

# Create your views here.
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
