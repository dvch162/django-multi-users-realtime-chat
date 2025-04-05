from django.forms import ModelForm
from django import forms
from .models import *

class CharMessageCreateForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Add message here...',
                'class': 'p-4 text-black form-control',
                'maxlength': 300,
                'autofocus': True,
            }),
        }