from django.db import models


class Menu(models.Model):
    restaurant = models.CharField(max_length=255)
    views = models.PositiveIntegerField(default=0)



class CardDetails(models.Model):
    cardNumber = models.DecimalField(max_digits = 10,decimal_places = 0, null = True)
    securityNumber = models.DecimalField(max_digits = 3,decimal_places = 0,null = True)
    cardHolderName = models.CharField(max_length = 50, null = True)
    expiryDate = models.DateField(null = True)
    pinNumber = models.DecimalField(max_digits = 4,decimal_places = 0,null = True)
