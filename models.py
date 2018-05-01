from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from appitems.otherModel import Menu
from accounts.models import Customer, Driver,Restaurant

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    tagname = models.CharField(max_length = 255)
    tagname2 = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE, related_name='menuitem')
    onoffer = models.BooleanField(default=False)
    usualcost = models.DecimalField(max_digits = 10, decimal_places=2)
    savings = models.DecimalField(max_digits = 10, decimal_places=2,null = True)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE, related_name = 'order')
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, related_name = 'orderdriver',null = True)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name = 'orderrestaurant',null = True)
    cost = models.DecimalField(max_digits = 100, decimal_places=2, null = True)


class OrderItem(models.Model):
    amount = models.IntegerField()
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='orderitem')
    order = models.ForeignKey(Order, on_delete = models.CASCADE,related_name= 'itemsorder')







