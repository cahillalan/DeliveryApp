from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Customer,Restaurant,Driver
from appitems.models import Menu, MenuItem
from django.views.generic import UpdateView, ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import resolve, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractUser
from django.http import Http404
from appitems.forms import MenuItemForm,OrderForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from deliveryapp.decorators import user_is_restaurant,user_is_customer,user_is_driver
from django import forms




def home(request):
    restaurants = Restaurant.objects.all()
    customers = Customer.objects.all()
    drivers = Driver.objects.all()
    rest_names = list()
    menu = Menu.objects.all()
    menu_list= list()

    for men in menu:
        menu_list.append(men.restaurant)

    for rest in restaurants:
        rest_names.append(rest.user.username)

    rest_names.append("end")
    for rest in customers:
        rest_names.append(rest.user.username)

    rest_names.append("end")

    for rest in drivers:
        rest_names.append(rest.user.username)

    response_html = '<br>'.join(rest_names)

    return HttpResponse(response_html)


##changed menulistview to definition view in order to use the decorators
@login_required
@user_is_customer
def MenuListView(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def MenuView(request, pk):
    menuitem = list()
    items = MenuItem.objects.all()
    for i in items:
        if i.menu.id is int(pk):
            menuitem.append(i)

    my_menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit = False)
            item.menu = my_menu
            item.save()
            form = MenuItemForm()

            menuitem = list()
            items = MenuItem.objects.all()
            for i in items:
                if i.menu.id is int(pk):
                    menuitem.append(i)
        return render(request, 'menu.html', {'menu': menuitem,'form': form})
    else:
        form = MenuItemForm()
    return render(request, 'menu.html', {'menu': menuitem,'form': form})


def CustomerMenuView(request, pk):
    menuitem = list()
    items = MenuItem.objects.all()
    for i in items:
        if i.menu.id is int(pk):
            menuitem.append(i)

    form = OrderForm()
    return render(request, 'customer_menu.html', {'menu': menuitem,'form':form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form = LoginForm()
                return render(request, 'login.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
