from django import forms
from django.contrib.auth.forms import UserCreationForm
from appitems.models import MenuItem
from django.contrib.auth.models import User



class SignInForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','password1')

class MenuItemForm(forms.ModelForm):
    name = forms.CharField(max_length=254, required=True)
    price = forms.DecimalField(required=True, decimal_places=2)
    class Meta(UserCreationForm.Meta):
        model = MenuItem
        fields = ('name', 'price')