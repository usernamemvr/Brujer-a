from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(label='Name',widget=forms.TextInput)
    DOB = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years=range(1900, 2023)))
    class Meta:
        model = User
        fields = ['username', 'name', 'DOB', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']        