from django import forms
from . import models


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name', 'description']
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
        }
