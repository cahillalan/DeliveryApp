from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from appitems.models import Menu
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render_to_response

from accounts.models import Customer, User, Restaurant

class CustomerSignUpForm(UserCreationForm):
    address = forms.CharField(max_length=254, required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'address')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.address = self.cleaned_data.get('address')
        customer.save()
        return user

class RestaurantSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2','first_name')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_restaurant = True
        user.save()
        rest = Restaurant.objects.create(user=user, menu = Menu.objects.create())
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
        return user

class RestaurantUpdateForm(forms.ModelForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name')

