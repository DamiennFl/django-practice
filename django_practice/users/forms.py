from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=40,
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        min_length=8,
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    confirm_password = forms.CharField(
        min_length=8,
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        min_length=8,
        max_length=50,
        required=False,
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
