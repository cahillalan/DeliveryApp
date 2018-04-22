from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from appitems.menuModel import Menu
from accounts.models import Customer, Driver,Restaurant

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now_add=True)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE, related_name='menuitem')


class OrderItem(models.Model):
    amount = models.IntegerField()
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='orderitem')

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE, related_name = 'order')
    items = models.ForeignKey(OrderItem, on_delete = models.CASCADE, related_name = 'onorder')
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, related_name = 'onorder')
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name = 'onorder')
    cost = models.DecimalField(max_digits = 100, decimal_places=2)

class AccountDetails(models.Model):
    cardNumber = models.DecimalField(max_digits = 10,decimal_places = 0)
    securityNumber = models.DecimalField(max_digits = 3,decimal_places = 0)
    cardHolderName = models.CharField(max_length = 50)
    expiryDate = models.DateField()
    pinNumber = models.DecimalField(max_digits = 4,decimal_places = 0)
    owner = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'accountOwner')




