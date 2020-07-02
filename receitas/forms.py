from django.forms import ModelForm, NumberInput, TextInput, Textarea
from .models import Receita

class ReceitaForm(ModelForm):
    class Meta:
        model  = Receita
        fields = ('nome', 'descricao', 'valor')
        labels = {
            'nome': 'Nome do capital recebido',
            'descricao': 'Descrição da receita',
            'valor': 'Valor da receita',
        }
        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Dê um nome ao dinheiro que vc quer registrar como entrada'}),
            'descricao': Textarea(attrs={'placeholder': 'Descreva a receita que deseja dar entrada com informações importantes de identificação'}),
            'valor': NumberInput(attrs={'class':'form-control', 'style': 'width: 50%;', 'step': '100.00', 'placeholder': 'Informe o valor da receita'}),
        }