from django import forms
from . import models


class InFlowForm(forms.ModelForm):

    class Meta:
        model = models.InFlow
        fields = ['supplier', 'product', 'quantity', 'description']
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
        widgets = {
            'supplier': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'product': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantity': forms.NumberInput(
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
