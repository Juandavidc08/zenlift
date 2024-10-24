from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['trainer', 'date', 'time']
        widgets = {
            'trainer': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make the trainer field readonly
        }
