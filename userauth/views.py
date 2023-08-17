from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login_page')
    
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def Signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.create_user(username, email, password)  # Use username, email, and password
            user.first_name = name
            user.save()
            messages.success(request, 'User created successfully')
            return redirect('login_page')
        except:
            messages.info(request, 'Username already exists')
            return redirect('Signup')  # Return the redirect function here
    
    return render(request, 'Sign-up.html')
