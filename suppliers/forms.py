from django import forms
from . import models


class SupplierForm(forms.ModelForm):

    class Meta:
        model = models.Supplier
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
