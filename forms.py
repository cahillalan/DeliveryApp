from django import forms

class SignInForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','password1')
