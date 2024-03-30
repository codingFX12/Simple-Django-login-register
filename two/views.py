from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Feature

def index(request):
    features = Feature.objects.all()

    return render(request, "index.html", {
        "features": features
    })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("login")
            
        else:
            messages.info(request, "confirm_password is wrong")
            return redirect("register")

    else:
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "username or password is wrong")
            return redirect("login")
    
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

