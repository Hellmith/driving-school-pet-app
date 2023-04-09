from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput

from .models import *


class CursantPostScheduleForm(forms.ModelForm):
    date_class = forms.DateField(
        widget=forms.SelectDateWidget(), label='Дата занятия')

    class Meta:
        model = Schedule
        fields = fields = ["id_worker",
                           "id_discipline", "date_class", "time_class"]


class WorkerPostUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'patronymic', 'date_of_birthday', 'id_region', 'id_city', 'id_street', 'house', 'apartment', 'tel', 'username',
             'is_cursant', 'id_post', 'is_worker'
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


class WorkerPostDisciplineForm(forms.ModelForm):

    class Meta:
        model = Discipline
        fields = '__all__'


class WorkerPostCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class WorkerPostCarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'


class WorkerPostRegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = '__all__'


class WorkerPostCityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = '__all__'


class WorkerPostStreetForm(forms.ModelForm):

    class Meta:
        model = Street
        fields = '__all__'


class SignupForm(UserCreationForm):
    is_worker = forms.BooleanField(widget=forms.HiddenInput(
        attrs={'readonly': True, 'value': 1}), required=False)
    id_post = forms.ModelChoiceField(queryset=Post.objects.all(
    ), widget=forms.HiddenInput(attrs={'readonly': True, 'value': 1}), required=False)

    class Meta:
        model = User
        fields = ["last_name", "first_name", "patronymic", "username",
                  "password1", "password2", "is_worker", 'id_post']
