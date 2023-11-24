from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': "form-control"
    }))


class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'form-control'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your password',
        'class': 'form-control'
    }))
