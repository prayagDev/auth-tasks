from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email']

class EditProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=["username", "first_name", "last_name", "email", "last_login", "date_joined"]

class AdminEditProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields="__all__"
