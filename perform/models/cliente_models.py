from django.db import models


class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=150)
    cnpj = models.CharField("CNPJ", max_length=18, unique=True)
    data_cadastro = models.DateTimeField("Data de Cadastro", auto_now_add=True)
    data_inicio_contrato = models.DateField("Data Início do Contrato")
    data_fim_contrato = models.DateField("Data Fim do Contrato", blank=True, null=True)
    data_fim_adendo = models.DateField("Data Fim do Adendo", blank=True, null=True)
    previsibilidade_operacional = models.CharField("Previsibilidade Operacional", max_length=255, blank=True, null=True)
    meta_contrato = models.DecimalField("Meta do Contrato", max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome
