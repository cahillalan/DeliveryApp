from django.db import models


class Menu(models.Model):
    restaurant = models.CharField(max_length=255)
    views = models.PositiveIntegerField(default=0)