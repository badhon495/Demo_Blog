from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User #whenever this form validates it will create a new user
        fields = ['username', 'email', 'password1', 'password2'] #which filed will be shown in the form