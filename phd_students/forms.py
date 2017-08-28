from django import forms
from .models import PhdStudent

class PhdStudentForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = {'total_student','awarded','submitted','pursuing'}
