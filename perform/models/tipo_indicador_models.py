from django.db import models

class TipoIndicador(models.Model):
    codigo = models.CharField("Código do Indicador", max_length=50, unique=True)
    descricao = models.CharField("Descrição do Indicador", max_length=150)

    def __str__(self):
        return self.descricao
