from django.core.exceptions import PermissionDenied
from .models import User

def user_is_customer(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_customer:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_restaurant(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_restaurant:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap



def user_is_driver(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_driver:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap