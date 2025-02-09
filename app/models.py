from django.db import models

# Modelo para o formulário de contato
class Contato(models.Model):
    nome = models.CharField(max_length=100)  # Campo de nome
    email = models.EmailField()  # Campo de e-mail
    mensagem = models.TextField()  # Campo de mensagem

    def __str__(self):
        return self.nome  # Retorna o nome como representação do objeto
