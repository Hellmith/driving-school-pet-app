from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput

from .models import User


class RegisterCadetForm(UserCreationForm):
    role = forms.CharField(widget=forms.HiddenInput(attrs={'readonly': True, 'value': 'cadet'}), required=False)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'patronymic', 'username', 'password1', 'password2', 'role']


class RegisterInstructorForm(UserCreationForm):
    role = forms.CharField(widget=forms.HiddenInput(attrs={'readonly': True, 'value': 'instructor'}), required=False)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'patronymic', 'username', 'password1', 'password2', 'role']


class RegisterOperForm(UserCreationForm):
    role = forms.CharField(widget=forms.HiddenInput(attrs={'readonly': True, 'value': 'oper'}), required=False)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'patronymic', 'username', 'password1', 'password2', 'role']
