from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import User, File


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File

        fields = ['file']
