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
from appitems.forms import MenuItemForm



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
    items = MenuItem.objects.all()
    for i in items:
        if i.menu.id is int(pk):
            menuitem.append(i)
            print(pk)


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
## deleted new menu class, not needed

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
