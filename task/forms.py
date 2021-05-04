from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','email','profile_pic']

