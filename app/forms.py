from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput
from django.conf import settings

from .models import *


# Форма регистрации
class SignupForm(UserCreationForm):
    is_worker = forms.BooleanField(widget=forms.HiddenInput(attrs={'readonly': True, 'value': 1}), required=False)
    id_post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput(attrs={'readonly': True, 'value': 1}), required=False)

    class Meta:
        model = User
        fields = ["last_name", "first_name", "patronymic", "username", "password1", "password2", "is_worker", 'id_post']

# Формы нахождение пользователей по группам
class WorkerGetUsersByGroupForm(forms.ModelForm):
    
    class Meta:
        model = Discipline
        fields = ['type_class']

# Формы расписание для курсантов
class CursantPostScheduleForm(forms.ModelForm):

    date_class = forms.DateField(input_formats=['%d.%m.%Y'], label='Дата занятия', widget=forms.DateInput(attrs={'placeholder': 'XX.XX.XXXX'}))
    time_class = forms.TimeField(input_formats=['%h:%m'], label='Время занятия', widget=forms.TimeInput(attrs={'placeholder': '00:00'}))

    class Meta:
        model = Schedule
        fields = fields = ["id_worker", "id_discipline", "date_class", "time_class"]


# Формы пользователи
class WorkerPostUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'patronymic', 'date_of_birthday', 'id_region', 'id_city', 'id_street', 'house', 'apartment', 'tel', 'username',
            'is_cursant', 'id_post', 'is_worker'
        ]


class WorkerUpdateUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'patronymic', 'date_of_birthday', 'id_region', 'id_city', 'id_street', 'house', 'apartment', 'tel', 'username',
            'is_cursant', 'id_post', 'is_worker', 'password'
        ]


# Формы должности
class WorkerPostPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


# Формы обучения
class WorkerPostTrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = '__all__'


# Формы вождения
class WorkerPostDrivingForm(forms.ModelForm):

    class Meta:
        model = Driving
        fields = '__all__'


# Формы курсов
class WorkerPostCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


# Формы дисциплин
class WorkerPostDisciplineForm(forms.ModelForm):

    class Meta:
        model = Discipline
        fields = '__all__'


# Формы категорий
class WorkerPostCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


# Формы машин
class WorkerPostCarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'


# Формы регионов
class WorkerPostRegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = '__all__'


# Формы городов
class WorkerPostCityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = '__all__'


# Формы улиц
class WorkerPostStreetForm(forms.ModelForm):

    class Meta:
        model = Street
        fields = '__all__'
