from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User #whenever this form validates it will create a new user
        fields = ['username', 'email', 'password1', 'password2'] #which filed will be shown in the form

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        Model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        Model = Profile
        fields = ['image']

