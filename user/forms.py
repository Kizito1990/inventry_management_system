from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "username"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["address", "phone", "image"]