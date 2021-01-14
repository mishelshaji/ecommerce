from django import forms
from django.forms import fields, widgets
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3'
                }
            ),
        }