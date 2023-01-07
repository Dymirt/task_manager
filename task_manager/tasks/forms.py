from django.forms import ModelForm, PasswordInput, TextInput
from .models import Organization


class OrganizationLoginForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['title', 'password']
        widgets = {
            'title': TextInput(attrs={
                'name': 'Title',
                'class': 'form-control mb-3',
            }),
            'password': PasswordInput(attrs={
                'name': 'Password',
                'class': 'form-control mb-3',
            }),
        }