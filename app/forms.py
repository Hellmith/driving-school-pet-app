from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput

from .models import *


class CursantPostScheduleForm(forms.ModelForm):
    date_class = forms.DateField(widget=forms.SelectDateWidget(), label='Дата занятия')

    class Meta:
        model = Schedule
        fields = fields = ["id_worker", "id_discipline", "date_class", "time_class"]


class WorkerPostUserForm(forms.ModelForm):
    date_of_birthday = forms.DateField(widget=forms.SelectDateWidget(), label='Дата рождения')

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'patronymic', 'date_of_birthday', 'id_region', 'id_city', 'id_street', 'house', 'apartment', 'tel', 'username',
            'password', 'is_cursant', 'id_post', 'is_worker'
        ]


class WorkerPostPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class WorkerPostTrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = '__all__'


class WorkerPostDrivingForm(forms.ModelForm):

    class Meta:
        model = Driving
        fields = '__all__'


class WorkerPostCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


# class WorkerUpdateUserForm(forms.ModelForm):
#     date_of_birthday = forms.DateField(widget=forms.SelectDateWidget(), label='Дата рождения')

#     class Meta:
#         model = User
#         fields = '__all__'


class SignupForm(UserCreationForm):
    is_worker = forms.BooleanField(widget=forms.HiddenInput(attrs={'readonly': True, 'value': 1}), required=False)
    id_post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput(attrs={'readonly': True, 'value': 1}), required=False)

    class Meta:
        model = User
        fields = ["last_name", "first_name", "patronymic", "username", "password1", "password2", "is_worker", 'id_post']
