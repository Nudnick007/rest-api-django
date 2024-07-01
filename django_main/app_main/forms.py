from django import forms
from django.forms import ClearableFileInput
from .models import Details

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('DocName', 'Doc')