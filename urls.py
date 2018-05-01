"""deliveryapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from accounts import views as accounts_views
from appitems import views as appitems_views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', appitems_views.home, name='home'),
    path('admin/', admin.site.urls),
    url(r'^signup/customer$', accounts_views.customer_signup, name='customer_signup'),
    url(r'^signup/restaurant$', accounts_views.restaurant_signup, name='restaurant_signup'),
    url(r'^signup/driver$', accounts_views.driver_signup, name='driver_signup'),
    url(r'^menulist/$', appitems_views.MenuListView, name='menu_view'),
    url(r'^offers/$', appitems_views.OffersListView, name='offers_view'),

    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^settings/account/restaurant/menu/(?P<pk>\d+)/$', appitems_views.MenuView, name='restaurant_menu'),
    url(r'^settings/account/restaurant$', accounts_views.RestaurantUpdateView.as_view(template_name='restaurant_account.html'), name='restaurant_account'),
    url(r'^settings/account/restaurant/statistics$', appitems_views.RestaurantStatisticsView, name='restaurant_statistics'),
    url(r'^settings/account/restaurant/address$', appitems_views.RestaurantAddressView, name='restaurant_address'),
    url(r'^settings/account/restaurant/menudelete/(?P<pk>\d+)/$', appitems_views.RestaurantDeleteMenuView,name='restaurant_menu_delete'),
    url(r'^settings/account/restaurant/menu/(?P<pk>\d+)/itemedit/(?P<pka>\d+)$', appitems_views.RestaurantEditItemView, name='restaurant_item_edit'),
    url(r'^settings/account/customer$', accounts_views.CustomerUpdateView.as_view(template_name='customer_account.html'),name='customer_account'),
    url(r'^settings/account/customer/address$',appitems_views.CustomerAddressView, name='customer_address'),
    url(r'^settings/account/customer/statistics$', appitems_views.CustomerStatisticsView, name='customer_statistics'),


    url(r'^settings/account/driver$', accounts_views.DriverUpdateView.as_view(template_name='driver_account.html'),name='driver_account'),
    url(r'^customer_menu/(?P<pk>\d+)/$', appitems_views.CustomerMenuView, name='customer_menu'),
    url(r'^order_confirmation/(?P<pk>\d+)$', appitems_views.OrderConfirmationView, name='order_confirmation'),
    url(r'^address_change/(?P<pk>\d+)$', appitems_views.AddressChangeView, name='address_change'),
    url(r'^card_change/(?P<pk>\d+)$', appitems_views.CardChangeView, name='card_change'),
    url(r'^order_dispatch/(?P<pk>\d+)$', appitems_views.OrderDispatchView, name='order_dispatch_info'),

    url(r'^settings/account/customer/carddetails$',accounts_views.CardDetailsView.as_view(template_name='card_details.html'), name='card_details'),

    ## added restaurant_account url
]
