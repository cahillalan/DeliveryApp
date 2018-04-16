from django.db import models


class Menu(models.Model):
    restaurant = models.CharField(max_length=255)
    views = models.PositiveIntegerField(default=0)

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now_add=True)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE, related_name='menuitem')
