from django import forms
from .models import Awards

class AwardForm(forms.ModelForm):
    class Meta:
        model = Awards
        fields ={ 'title', 'organisation', 'month', 'year' }
