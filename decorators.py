from django.core.exceptions import PermissionDenied
from accounts.models import User

def user_is_customer(function):
    def wrap(request, *args):
        user = request.user
        if user.is_customer:
            return function(request, *args)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_restaurant(function):
    def wrap(request,*args):
        my_user = request.user
        if my_user.is_restaurant is True:
            print("ALAN")
            return function(request, *args )
        else:
            print(my_user.is_restaurant)
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap



def user_is_driver(function):
    def wrap(request, *args):
        user = request.user
        if user.is_driver:
            return function(request, *args)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap