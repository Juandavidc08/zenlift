from django import forms
from .models import Appointment
from django.core.exceptions import ValidationError
from datetime import datetime

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

    # Validate that the date and time are in the future
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.now().date():
            raise ValidationError("You cannot book a past date.")
        return date

    def clean_time(self):
        time = self.cleaned_data['time']
        # Add any other logic to restrict odd hours here
        if time < datetime.now().time() and self.cleaned_data.get('date') == datetime.now().date():
            raise ValidationError("The time cannot be in the past.")
        return time
