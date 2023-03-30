from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput

from .models import Schedule


class CursantPostSchedule(forms.ModelForm):
    id_worker = forms.TimeField(widget=forms.HiddenInput(attrs={'readonly': True}), required=False)
    id_discipline = forms.TimeField(widget=forms.HiddenInput(attrs={'readonly': True}), required=False)
    date_class = forms.DateField(widget=forms.HiddenInput(attrs={'readonly': True}), required=False)
    time_class = forms.TimeField(widget=forms.HiddenInput(attrs={'readonly': True}), required=False)

    class Meta:
        model = Schedule
        fields = fields = ["id_worker", "id_discipline", "date_class", "time_class"]
