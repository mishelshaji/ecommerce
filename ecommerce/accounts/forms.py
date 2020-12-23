from django import forms
from django.forms import widgets
from .models import User, CustomerDetails

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        exclude = ['user']
        widgets = {
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'pin': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'city': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }