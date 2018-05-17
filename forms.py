from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from appitems.otherModel import Menu,CardDetails
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render_to_response

from accounts.models import Customer, User, Restaurant,Driver

class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user,cardDetails = CardDetails.objects.create(id = user.id))
        customer.save()

        return user

class RestaurantSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_restaurant = True
        user.save()
        rest = Restaurant.objects.create(user=user, menu = Menu.objects.create(id = user.id, views = 0))
        rest.save()

        return user

class DriverSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.save()
        driver = Driver.objects.create(user=user)
        driver.save()
        return user


