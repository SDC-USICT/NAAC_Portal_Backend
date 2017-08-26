from django import forms
from .models import Patents


class PatentForm(forms.ModelForm):
    class Meta:
        model = Patents
        fields = ('name', 'patenting_agency', 'year_application', 'year_grant')
