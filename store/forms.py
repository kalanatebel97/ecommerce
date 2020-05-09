from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import login, authenticate
from django import forms
from .models import CustomUser

# from store.models import CustomUser


class RegisterForm(UserCreationForm):
    mobile_number = forms.CharField()
    city = forms.CharField()

    class Meta(UserCreationForm):
      model = CustomUser
      fields = ["username", "email" ,"mobile_number","city"]

# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('email',)