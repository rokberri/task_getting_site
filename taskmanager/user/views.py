from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout



def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("tiket:list")
    else:
        form = UserCreationForm()
    return render(request, 'user/register_form.html', {'form':form })


def user_list(request):
    return HttpResponse('No users yet(')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("tiket:list")
    else: 
        form = AuthenticationForm()

    return render(request, 'user/login.html', {'form':form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("tiket:list")
