from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    mensagem = models.CharField(max_length=150)
    log_data = models.DateTimeField("Data gravada")
    
    def __str__(self):
        data = timezone.localtime(self.log_data)
        return f"'{self.mensagem}' gravado em \
        {data.strftime('%A, %d %B, %Y %X')}"

class CadastroClientes(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
