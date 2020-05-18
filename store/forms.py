from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import CustomUser

class RegisterForm(UserCreationForm):
    mobile_number = forms.IntegerField()
    city = forms.CharField()

    class Meta(UserCreationForm):
      model = CustomUser
      fields = (
          "username",
          "first_name",
          "last_name",
          "email",
          "mobile_number",
          "city",
          "password1",
          "password2"
      )
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('email',)