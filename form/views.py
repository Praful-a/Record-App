from django.shortcuts import render, redirect
from .models import Emp
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 and first_name and email and username:
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, f'Username is already exists!')
                    return redirect('record:register')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, f'Email is already exists!')
                    return redirect('record:register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name, email=email, password=password1, username=username)
                    user.save()

                    return redirect('record:login')
            else:
                messages.error(request, f'Password does not match!')
                return redirect('record:register')
        else:
            messages.error(request, f'All Fields are required!')
            return redirect('record:register')
    else:

        return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('record:home')
        else:
            messages.error(request, f'Something went wrong!')
            return redirect('record:login')
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('record:home')


def home(request):
    return render(request, "home.html")


def add(request):
    return render(request, "add.html")


def record(request):
    return render(request, "record.html")
