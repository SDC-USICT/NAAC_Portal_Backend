from django import forms
from .models import GuestLecture

class GuestLecturerForm(forms.ModelForm):
    class Meta:
        model = GuestLecture
        fields = { 'nature','institute', 'date', 'topic'}
        
