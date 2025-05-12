from django.db import models

class TipoFaturamento(models.Model):
    nome = models.CharField("Nome do Tipo de Faturamento", max_length=100, unique=True)

    def __str__(self):
        return self.nome
