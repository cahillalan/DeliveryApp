from django.contrib.auth.models import AbstractUser
from django.db import models
from appitems.models import Menu

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu')


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    vehiclereg = models.CharField(max_length=255)