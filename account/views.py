from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from stories.models import Recipe
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect(reverse_lazy("account:login"))
    else:
        form = RegisterForm()

    context = {
        "form": form
    }
    
    return render(request, 'register.html', context)


def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data["email"], password=form.cleaned_data["password"])
            if user:
                django_login(request, user)
                return redirect(reverse_lazy("account:profile"))
    else: form = LoginForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context)


@login_required
def profile(request):
    
    return render(request, "user-profile.html")

@login_required
def logout(request):
    
    django_logout(request)
    return redirect(reverse_lazy("account:login"))   