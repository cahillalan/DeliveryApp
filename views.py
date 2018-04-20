from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from django.contrib.auth import login as auth_login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy


from .forms import CustomerSignUpForm,RestaurantSignUpForm,DriverSignUpForm
from .models import User
from django.http import HttpResponse
from .models import Customer,Restaurant


def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            customer = form.save()
            auth_login(request, customer)
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


@method_decorator(login_required, name='dispatch')
class RestaurantUpdateView(UpdateView):
    model = User
    fields = ('username','first_name' )
    template_name= 'restaurant_account.html'
    success_url = reverse_lazy('restaurant_account')

    def get_object(self):
        return self.request.user
## added in the updatviews below

@method_decorator(login_required, name='dispatch')
class CustomerUpdateView(UpdateView):
    model = User
    fields = ('username','first_name' )
    template_name= 'customer_account.html'
    success_url = reverse_lazy('customer_account')

    def get_object(self):
        return self.request.user

@method_decorator(login_required, name='dispatch')
class DriverUpdateView(UpdateView):
    model = User
    fields = ('username','first_name' )
    template_name= 'driver_account.html'
    success_url = reverse_lazy('driver_account')

    def get_object(self):
        return self.request.user
