from django import forms
from hello_world.models import LogMessage, CadastroClientes

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("mensagem",)

class CadastroClientesForm(forms.ModelForm):
    class Meta:
        model = CadastroClientes
        fields = ("nome", "cpf", "telefone",)