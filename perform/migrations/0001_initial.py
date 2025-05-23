# Generated by Django 5.2.1 on 2025-05-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('cnpj', models.CharField(max_length=18, unique=True, verbose_name='CNPJ')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('data_inicio_contrato', models.DateField(verbose_name='Data Início do Contrato')),
                ('data_fim_contrato', models.DateField(blank=True, null=True, verbose_name='Data Fim do Contrato')),
                ('data_fim_adendo', models.DateField(blank=True, null=True, verbose_name='Data Fim do Adendo')),
                ('previsibilidade_operacional', models.CharField(blank=True, max_length=255, null=True, verbose_name='Previsibilidade Operacional')),
                ('meta_contrato', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Meta do Contrato')),
            ],
        ),
    ]
