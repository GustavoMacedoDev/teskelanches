from django import forms
from input_mask.widgets import InputMask

from sistema.models import Caixa


class DataCustomInput(InputMask):
    mask = {
        'mask': '99/99/9999',
    }


class CaixaForm(forms.ModelForm):
    data_abertura = forms.DateField(widget=DataCustomInput(
            attrs={'class': 'form-control', 'data-mask': '00/00/0000', 'required': 'true'}), label="Data de Abertura")

    data_fechamento = forms.DateField(widget=DataCustomInput(
        attrs={'class': 'form-control', 'data-mask': '00/00/0000'}), label="Data de Fechamento")

    observacao = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'required':'true'}), label="Observação")

    class Meta:
        model = Caixa
        fields = ['data_abertura', 'data_fechamento', 'observacao']