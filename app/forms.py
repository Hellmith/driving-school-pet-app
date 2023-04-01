from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput

from .models import Schedule


class CursantPostScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = fields = ["id_worker", "id_discipline", "date_class", "time_class"]
