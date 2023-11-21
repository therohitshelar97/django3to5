from django import forms
from .models import django_abc
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class abc_form(forms.ModelForm):
    class Meta:
        model = django_abc
        fields = '__all__'

class SignUp_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
