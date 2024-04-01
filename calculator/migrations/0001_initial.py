# Generated by Django 4.0.3 on 2024-04-01 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_type', models.CharField(choices=[('Residencial', 'Residencial'), ('Comercial', 'Comercial'), ('Industrial', 'Industrial')], max_length=20, verbose_name='Tipo de Consumidor')),
                ('consumption_range', models.CharField(choices=[('<10000', 'Menor que 10.000 kWh'), ('10000-20000', '10.000 kWh - 20.000 kWh'), ('>20000', 'Maior que 20.000 kWh')], max_length=20, verbose_name='Intervalo de Consumo')),
                ('cover_value', models.FloatField(verbose_name='Valor de Cobertura')),
                ('discount_value', models.FloatField(verbose_name='Valor de Desconto')),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nome')),
                ('document', models.CharField(max_length=14, unique=True, verbose_name='Documento (CPF/CNPJ)')),
                ('city', models.CharField(max_length=100, verbose_name='Cidade')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
                ('consumption', models.IntegerField(verbose_name='Consumo (kWh)')),
                ('consumer_type', models.CharField(max_length=20, verbose_name='Tipo')),
                ('cover_value', models.FloatField(verbose_name='Cobertura (%)')),
                ('distributor_tax', models.FloatField(verbose_name='Tarifa da Distribuidora')),
                ('discount_rule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calculator.discountrule', verbose_name='Regra de Desconto')),
            ],
        ),
    ]