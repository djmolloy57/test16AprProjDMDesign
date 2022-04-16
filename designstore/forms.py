from django import forms 
from .models import TestItems 

class ItemForm(forms.ModelForm):
    class Meta:
        model = TestItems 
        fields = ['name', 'done']