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
from appitems.otherModel import CardDetails
from django.db import models


from .forms import CustomerSignUpForm,RestaurantSignUpForm,DriverSignUpForm
from .models import User
from django.http import HttpResponse
from .models import Customer,Restaurant,Driver


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
    fields = ('username',)
    template_name= 'restaurant_account.html'
    success_url = reverse_lazy('restaurant_account')

    def get_object(self):
        return self.request.user
## added in the updatviews below

@method_decorator(login_required, name='dispatch')
class ExtendedRestaurantUpdateView(UpdateView):
    model = Restaurant
    fields = ('name', 'contactnumber','managersName','typeoffood')
    template_name = 'extended_restaurant_account.html'
    success_url = reverse_lazy('extended_restaurant_account')

    def get_object(self):
        rest = Restaurant.objects.get(user = self.request.user)
        return rest

@method_decorator(login_required, name='dispatch')
class CustomerUpdateView(UpdateView):
    model = User
    fields = ('username', )
    template_name= 'customer_account.html'
    success_url = reverse_lazy('customer_account')

    def get_object(self):
        return self.request.user


@method_decorator(login_required, name='dispatch')
class ExtendedCustomerUpdateView(UpdateView):
    model = Customer
    fields = ('firstname','lastname','contactnumber' )
    template_name= 'extended_customer_account.html'
    success_url = reverse_lazy('extended_customer_account')

    def get_object(self):
        cust = Customer.objects.get(user=self.request.user)
        return cust

@method_decorator(login_required, name='dispatch')
class DriverUpdateView(UpdateView):
    model = User
    fields = ('username','first_name' )
    template_name= 'driver_account.html'
    success_url = reverse_lazy('driver_account')

    def get_object(self):
        return self.request.user

@method_decorator(login_required, name='dispatch')
class ExtendedDriverUpdateView(UpdateView):
    model = Driver
    fields = ('vehiclereg','typeofvehicle','contactnumber' )
    template_name= 'extended_driver_account.html'
    success_url = reverse_lazy('driver_account')

    def get_object(self):
        driver = Driver.objects.get(user = self.request.user)
        return driver

@method_decorator(login_required, name='dispatch')
class CardDetailsView(UpdateView):
    model = CardDetails
    fields = ('cardNumber','securityNumber','cardHolderName','expiryDate','pinNumber' )
    template_name= 'card_details.html'
    success_url = reverse_lazy('card_details')

    def get_object(self):
        instance = self.request.user
        cust = Customer.objects.get(user = instance)
        card = cust.cardDetails
        return card
