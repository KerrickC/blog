#need this for new fields in register

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'autofocus': True}))
    #location_zip = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')



class UserUpdateForm(forms.ModelForm):
    company = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    location_zip = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ['location_zip', 'image']
        