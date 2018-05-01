from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Customer,Restaurant,Driver
from appitems.models import MenuItem,Order,OrderItem
from appitems.otherModel import Menu,CardDetails
from django.views.generic import UpdateView, ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import resolve, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractUser
from django.http import Http404
from appitems.forms import MenuItemForm,ItemEditForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from deliveryapp.decorators import user_is_restaurant,user_is_customer,user_is_driver
from django import forms
from statistics import mode




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
    rest= Restaurant.objects.all()
    restaurants = list()
    for r in rest:
        if r.address is not None:
            restaurants.append(r)
            # this ensures all restaurants listed have a valid address. (addresses are authenticated on input)
    return render(request, 'home.html', {'restaurants': restaurants})

def OffersListView(request):
    offers = MenuItem.objects.filter(onoffer=True).order_by('menu')
    return render(request, 'offers.html', {'items': offers})

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
            item.tagname = item.name.replace(" ", "")+str(item.id)
            item.tagname2 = item.name.replace(" ", "")+str(item.id)
            cost = form.cleaned_data['price']
            item.usualcost = cost
            print(cost)
            print(item.usualcost)
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
    if request.method == 'POST':
        order = request.POST
        print(order)
        taggeditems = list()
        for i in order:
            taggeditems.append(i)
        if len(taggeditems) is 1:
            return render(request, 'customer_menu.html', {'menu': menuitem})
        else:
            print (taggeditems)
            ord = Order.objects.create(customer=Customer.objects.get(user = request.user), restaurant = Restaurant.objects.get(pk = pk))
            #for statement necessary becaue other restaurants might have the same items.
            totalcost = 0
            for a in taggeditems:
                for i in menuitem:
                    if str(i.tagname) == str(a):

                        orderitem = OrderItem.objects.create(item=i,order = ord,amount = order[i.tagname][0])
                        cost = (float(orderitem.item.price) * float(orderitem.amount))

                        totalcost = totalcost + cost
                        print(totalcost)
            ord.cost = totalcost
            ord.save()
            return redirect('order_confirmation', pk=ord.pk)

    else:
        menu = Menu.objects.get(pk = pk)
        view = menu.views
        view = view + 1
        menu.views = view
        menu.save()
        return render(request, 'customer_menu.html', {'menu': menuitem})


def OrderConfirmationView(request,pk ):

    order = get_object_or_404(Order, pk=pk)
    orderitems = OrderItem.objects.filter(order = order)

    if request.method == 'POST':

        return redirect('address_change', pk=order.pk)
    else:
        return render(request, 'order_confirmation.html',{'order':order,'items':orderitems})

def AddressChangeView(request,pk ):

    customer = Customer.objects.get(user =request.user)

    if request.method == 'POST':
        addr = request.POST.get('coordinates')
        positions = addr.split(",")
        check = True
        north = positions[0].lstrip('(')
        print(float(north))
        lat = positions[1].strip(')')
        print(lat)
        if float(north) < 52.82052:
            print(1)
            check = False
        elif float(north) > 52.865709:
            print(2)
            check = False
        elif float(lat) < -6.981831999994:
            print(3)
            check = False
        elif float(lat) > -6.84460999999:
            print(4)
            check = False

        print(check)
        if check is True:
            customer.address = addr
            customer.save()
            return redirect('card_change', pk = pk)
        else:
            return redirect('address_change', pk=pk)
    else:
        return render(request, 'address_change1.html', {'cust': customer})


def CardChangeView(request,pk ):

    customer = Customer.objects.get(user =request.user)
    card = customer.cardDetails

    if request.method == 'POST':
        num = request.POST['cardNumber']
        secnum = request.POST['securityNumber']
        name = request.POST['CardHolderName']
        pin = request.POST['pinNumber']
        card.cardNumber = num
        card.securityNumber = secnum
        card.cardHolderName = name
        card.pinNumber = pin
        card.save()

        return redirect('order_dispatch_info', pk = pk)
    else:
        return render(request, 'card_change.html',{'card':card})


## added Address views which are google map pages
def OrderDispatchView(request,pk):
    order = Order.objects.get(pk = pk)
    cust = Customer.objects.get(user = request.user)
    adr1 = cust.address
    adr2 = order.restaurant.address
    my_addresses = list()
    my_addresses.append(adr1)
    my_addresses.append(adr2)
    return render(request, 'order_dispatch.html', {'addresses': my_addresses, 'order':order,'cust' :cust })


def CustomerStatisticsView(request):
    customer = Customer.objects.get(user =request.user)
    orders = Order.objects.filter (customer = customer)
    orderitems = OrderItem.objects.all()
    ordercount = 0
    itemnumberlist = list()
    itemcount = 0
    restaurantnumbers = list()
    drivernumbers = list()

    for o in orders:
        ordercount += 1
        restaurantnumbers.append(o.restaurant.user.id)
        print(ordercount)
        for i in orderitems:
            if i.order.id == o.id:
                itemnumberlist.append(i.item.id)
                itemcount +=1
    itemnum = mode(itemnumberlist)
    favitem = MenuItem.objects.get(id = itemnum)
    restnum = mode(restaurantnumbers)
    favrest = Restaurant.objects.get(user_id = restnum)

    return render(request, 'customer_statistics.html', {'count':ordercount,'favitem':favitem,'favrest':favrest,'itemcount':itemcount})

def RestaurantStatisticsView(request):
    restaurant = Restaurant.objects.get(user =request.user)
    orders = Order.objects.filter (restaurant = restaurant)
    orderitems = OrderItem.objects.all()
    ordercount = 0
    itemnumberlist = list()
    itemcount = 0
    customernumbers = list()
    drivernumbers = list()

    for o in orders:
        ordercount += 1
        customernumbers.append(o.customer.user.id)
        for i in orderitems:
            if i.order.id == o.id:
                itemnumberlist.append(i.item.id)
                itemcount +=1
    itemnum = mode(itemnumberlist)
    favitem = MenuItem.objects.get(id = itemnum)
    restnum = mode(customernumbers)
    favcust = Customer.objects.get(user_id = restnum)
    views = restaurant.menu.views
    percentageofsales = ((ordercount/views)*100)
    return render(request, 'restaurant_statistics.html', {'views':views,'count':ordercount,'percent':percentageofsales,'favitem':favitem,'favcust':favcust,'itemcount':itemcount})



def CustomerAddressView(request):

    customer = Customer.objects.get(user =request.user)

    if request.method == 'POST':
        addr = request.POST.get('coordinates')
        customer.address = addr.replace(" ", "")
        positions = addr.split(",")
        check = True
        north = positions[0].lstrip('(')
        print(float(north))
        lat = positions[1].strip(')')
        print(lat)
        if float(north) < 52.82052:
            print(1)
            check = False
        elif float(north) > 52.865709:
            print(2)
            check = False
        elif float(lat) < -6.981831999994:
            print(3)
            check = False
        elif float(lat) > -6.84460999999:
            print(4)
            check = False

        print(check)
        if check is True:

            customer.save()
            return redirect('customer_account')
        else:
            return render(request, 'customer_address.html', {'cust': customer})

    else:
        return render(request, 'customer_address.html',{'cust':customer})

def RestaurantAddressView(request):

    restaurant = Restaurant.objects.get(user =request.user)

    if request.method == 'POST':
        addr = request.POST.get('coordinates')
        restaurant.address = addr.replace(" ", "")

        positions = addr.split(",")
        check = True
        north = positions[0].lstrip('(')
        print(float(north))
        lat = positions[1].strip(')')
        print(lat)
        if float(north) < 52.82052:
            print(1)
            check = False
        elif float(north) > 52.865709:
            print(2)
            check = False
        elif float(lat) < -6.981831999994:
            print(3)
            check = False
        elif float(lat) > -6.84460999999:
            print(4)
            check = False

        print(check)
        if check is True:

            restaurant.save()
            return redirect('restaurant_account')
        else:
            return render(request, 'restaurant_address.html', {'rest': restaurant})
    else:
        return render(request, 'restaurant_address.html',{'rest':restaurant})
##added the delete item view for the menus
def RestaurantDeleteMenuView(request, pk):
    menuitem = list()
    restaurant = Restaurant.objects.get(user =request.user)
    items = MenuItem.objects.all()
    print(restaurant.menu.id)
    for i in items:
        print(i.menu.id)
        if i.menu.id is restaurant.menu.id:
            menuitem.append(i)
    if request.method == 'POST':
        deleted = request.POST
        deleteditems = list()
        for d in deleted:
            deleteditems.append(d)
        if len(deleteditems) is 1:
            return render(request, 'restaurant_delete_menu.html', {'menu': menuitem})
        else:
            for d in deleteditems:
                for i in items:
                    if str(i.tagname) == str(d):
                        i.delete()

            return redirect('restaurant_account')

    else:
        return render(request, 'restaurant_delete_menu.html', {'menu': menuitem})

def RestaurantEditItemView(request, pk,pka):
    menuitem = MenuItem.objects.get(pk =pka)

    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            if item.onoffer is True:

                menuitem.price = item.price
                p = menuitem.price
                op = menuitem.usualcost
                print(op)
                print(p)
                print(menuitem.name)
                save = op - p
                menuitem.savings = save
                menuitem.onoffer=True
                print(menuitem.savings)
                menuitem.save()
                return redirect('restaurant_menu',pk = pk)
            else:
                menuitem.onoffer =False
                menuitem.price = usualprice
                menuitem.save()

                return redirect('restaurant_menu',pk = pk)


    else:
        form = ItemEditForm()
        return render(request, 'item_edit.html', {'menu': menuitem,'form':form})


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

