from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import login as auth_login

from .forms import CustomerSignUpForm,RestaurantSignUpForm,DriverSignUpForm
from .models import User
from django.http import HttpResponse
from .models import Customer


def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
        return redirect('home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'customer_signup.html', {'form': form})

def restaurant_signup(request):
    if request.method == 'POST':
        form = RestaurantSignUpForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            auth_login(request, restaurant)
        return redirect('home')
    else:
        form = RestaurantSignUpForm()
    return render(request, 'restaurant_signup.html', {'form': form})

def driver_signup(request):
    if request.method == 'POST':
        form = DriverSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
        return redirect('home')
    else:
        form = DriverSignUpForm()
    return render(request, 'driver_signup.html', {'form': form})

