from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.http import HttpResponse


def create_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            email = form.cleaned_data["email"]
            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return redirect("users:create_user")  # The webpage

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect("users:create_user")

            if User.objects.filter(email=email).exists():
                messages.error(request, "An account with this email already exists.")
                return redirect("users:create_user")

            # Do only if things match.
            User.objects.create_user(username=username, password=password, email=email)
            messages.success(request, "User created successfully.")
            # PLACEHOLDER, return actuall html once created.
            return redirect("users:login")
    else:
        form = UserRegistrationForm()
        return render(request, "accounts/create_user.html", {"form": form})


def logout(request):
    logout(request)
    return redirect("homepage")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return messages.error(request, "Invalid username or password.")
    return render(request, "users/login.html")
