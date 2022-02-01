from dataclasses import field
from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Project
        fields=('category',)