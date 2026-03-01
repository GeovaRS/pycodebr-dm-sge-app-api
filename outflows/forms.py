from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutFlowForm(forms.ModelForm):

    class Meta:
        model = models.OutFlow
        fields = ['product', 'quantity', 'description']
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
        widgets = {
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

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'Quantidade em estoque para produto {product.title} é de {product.quantity} unidades.'
            )

        return quantity
