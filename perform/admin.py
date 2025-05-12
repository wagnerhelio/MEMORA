from django.contrib import admin
from perform.models import Cliente,TipoFaturamento, TipoIndicador, Faturamento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'cnpj',
        'data_inicio_contrato',
        'data_fim_contrato',
        'data_fim_adendo',
        'previsibilidade_operacional',
        'meta_contrato',
    )
    search_fields = ('nome', 'cnpj')
    list_filter = ('data_inicio_contrato', 'data_fim_contrato')

@admin.register(TipoFaturamento)
class TipoFaturamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(TipoIndicador)
class TipoIndicadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    search_fields = ('codigo', 'descricao')

@admin.register(Faturamento)
class FaturamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'contrato', 'indicador', 'ano_referencia')
    list_filter = ('contrato', 'indicador', 'ano_referencia')
    search_fields = ('contrato__nome', 'indicador__descricao')