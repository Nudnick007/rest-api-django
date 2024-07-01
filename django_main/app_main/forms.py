from django import forms
from django.forms import ClearableFileInput
from .models import document

class DetailsForm(forms.ModelForm):
    class Meta:
        model = document
        fields = ('DocName', 'Doc')