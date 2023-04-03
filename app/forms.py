from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput

from .models import Schedule, User, Post


class CursantPostScheduleForm(forms.ModelForm):
    date_class = forms.DateField(widget=forms.SelectDateWidget(), label='Дата занятия')

    class Meta:
        model = Schedule
        fields = fields = ["id_worker", "id_discipline", "date_class", "time_class"]


class SignupForm(UserCreationForm):
    is_worker = forms.BooleanField(widget=forms.HiddenInput(attrs={'readonly': True, 'value': 1}), required=False)
    id_post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput(attrs={'readonly': True, 'value': 1}), required=False)

    class Meta:
        model = User
        fields = ["last_name", "first_name", "patronymic", "username", "password1", "password2", "is_worker", 'id_post']
