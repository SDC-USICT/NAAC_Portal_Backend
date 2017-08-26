from django import forms
from .models import GuestLecturer

class GuestLecturerForm(forms.ModelForm):
    class Meta:
        model = GuestLecturer
        fields = { 'nature','institute', 'date', 'topic'}
        
