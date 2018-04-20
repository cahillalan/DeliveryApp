from django import forms
from django.contrib.auth.forms import UserCreationForm
from appitems.models import MenuItem
from django.contrib.auth.models import User
from accounts.models import Customer,Restaurant,Driver



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


class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.add_fields()


    def add_fields(self):
        # generate a queryset of the activities to show
        # could be sorted if a special order is needed
        items = MenuItem.objects.all()
        if not items:
            return

        for a in items:
            # required false is important to allow the field NOT to be checked
            myfields = list()
            self.fields[a.id]=forms.BooleanField(label=a.name, required=False)
            self.fields[a.name] = forms.IntegerField(label='amount',required = True)