from django import forms
from django.contrib.auth.forms import UserCreationForm
from appitems.models import MenuItem
from django.contrib.auth.models import User
from accounts.models import Customer,Restaurant,Driver
from appitems.otherModel import Menu



class SignInForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','password1')

class MenuItemForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)
    price = forms.DecimalField(required=True, decimal_places=2)
    class Meta(UserCreationForm.Meta):
        model = MenuItem
        fields = ('name', 'price')


class OrderForm(forms.Form):
    def __init__(self,pk, *args, **kwargs):
        print('justin')
        print(pk)

        super(OrderForm, self).__init__(*args, **kwargs)
        print('super Call')
        print(pk)
        self.pk = pk
        print('After Call')
        print (pk)
        print('HERE HHHHHHHH')
        self.add_fields(pk)


    def add_fields(self,pk):
        # generate a queryset of the activities to show
        # could be sorted if a special order is needed
        items = MenuItem.objects.filter(menu=pk)
        if not items:
            return

        for a in items:
            # required false is important to allow the field NOT to be checked
            self.fields[a.id] = forms.BooleanField(label=a.name, required=False)
            self.fields[a.name] = forms.IntegerField(label='amount',required = True)


