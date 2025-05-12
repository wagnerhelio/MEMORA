from django.db import models
from .tipo_faturamento_models import TipoFaturamento
from .tipo_indicador_models import TipoIndicador

class Faturamento(models.Model):
    contrato = models.ForeignKey(TipoFaturamento, on_delete=models.CASCADE)
    indicador = models.ForeignKey(TipoIndicador, on_delete=models.CASCADE)
    ano_referencia = models.IntegerField()

    valor_jan = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_fev = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_mar = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_abr = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_mai = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_jun = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_jul = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_ago = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_set = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_out = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_nov = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_dez = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.contrato} - {self.indicador} ({self.ano_referencia})'
