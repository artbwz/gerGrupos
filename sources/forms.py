from django import forms

class TarefaForm(forms.Form):
    descricao = forms.CharField(label='Descrição da Tarefa', max_length=200)
    data_entrega = forms.DateField(label='Data de Entrega')
