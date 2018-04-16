from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Customer,Restaurant
from appitems.models import Menu, MenuItem
from django.views.generic import UpdateView, ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import resolve, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractUser
from django.http import Http404



def home(request):
    restaurants = Restaurant.objects.all()
    rest_names = list()
    menu = Menu.objects.all()
    menu_list= list()

    for men in menu:
        menu_list.append(men.restaurant)

    for rest in restaurants:
        rest_names.append(str(rest.user.id))

    print(rest_names)

    response_html = '<br>'.join(rest_names)

    return HttpResponse(response_html)

class MenuListView(ListView):
    model = Restaurant
    context_object_name = 'restaurants'
    template_name = 'home.html'


def MenuView(request, pk):

    menuitem = list()
    item = MenuItem.objects.all()
    for i in item:
        if i.id is 1:
            menuitem.append(i)

    return render(request, 'menu.html', {'menu': menuitem})

@login_required
def new_menu(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = NewMenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.restaurant = restaurant
            menu.save()
            return redirect('MenuListView')
    else:
        form = NewMenuForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


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
