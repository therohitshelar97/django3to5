from django import forms
from .models import django_abc

class abc_form(forms.ModelForm):
    class Meta:
        model = django_abc
        fields = '__all__'
