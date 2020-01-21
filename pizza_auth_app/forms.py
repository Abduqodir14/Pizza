from pizza_auth_app.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password1",
        )
