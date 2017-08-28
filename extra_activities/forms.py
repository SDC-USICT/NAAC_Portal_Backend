from django import forms
from .models import Extra

class ExtraForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = {'name','department','details','year'}
