from django.contrib.auth.models import AbstractUser
from django.db import models
from appitems.otherModel import Menu,CardDetails
from datetime import datetime

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name = 'cust')
    address = models.CharField(max_length=255)
    cardDetails = models.ForeignKey(CardDetails , on_delete = models.CASCADE, related_name = 'card_details')
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu')
    name = models.CharField(max_length = 255)
    contactnumber = models.PositiveIntegerField(default=0)
    managersName = models.CharField(max_length = 255)
    typeoffood = models.CharField(max_length = 255)


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    vehiclereg = models.CharField(max_length=255)
    typeofvehicle = models.CharField(max_length = 255)
    lastdelivery = models.DateTimeField(default=datetime.now(), blank=True)
    availablefordelivery= models.BooleanField(default=True)

