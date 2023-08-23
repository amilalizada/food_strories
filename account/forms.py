from django import forms
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import fields
from django.forms import widgets
from .models import User

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm Password"
    }))
    class Meta:

        model = User

        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "bio",
            "image",
            "password",
            "confirm_password",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            }),
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username"
            }),
            "bio": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Bio"
            }),
            "image": forms.FileInput(attrs={
                "class": "form-control"
            }),
            "password": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Password"
            })
        }
    
    def clean(self):
        data = self.cleaned_data
        if data["password"] != data["confirm_password"]:
            self.add_error("confirm_password", "Password does not match")

        return super().clean()


class LoginForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "email"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password"
    }))