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
    url(r'^menulist/$', appitems_views.MenuListView.as_view(), name='menu_view'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^menu/(?P<pk>\d+)/$', appitems_views.MenuView, name='restaurant_menu'),
    url(r'^settings/account/$', accounts_views.RestaurantUpdateView.as_view(template_name='restaurant_account.html'), name='restaurant_account'),
## added restaurant_account url
]
