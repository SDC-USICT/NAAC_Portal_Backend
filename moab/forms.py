from django import forms
from .models import Membership

class MoabForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields ={ 'type', 'academic_body', 'university_agency'}
