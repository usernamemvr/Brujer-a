from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name',widget=forms.TextInput)
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput)
    DOB = forms.DateField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'DOB', 'email', 'password1', 'password2']
