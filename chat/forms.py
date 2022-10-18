from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'first_name', 'email', 'password1', 'password2',  ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }