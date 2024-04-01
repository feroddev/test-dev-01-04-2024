from django.db import models


# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""


class DiscountRule(models.Model):
    consumer_type_choices = [
        ("Residencial", "Residencial"),
        ("Comercial", "Comercial"),
        ("Industrial", "Industrial"),
    ]
    consumption_range_choices = [
        ("<10000", "Menor que 10.000 kWh"),
        ("10000-20000", "10.000 kWh - 20.000 kWh"),
        (">20000", "Maior que 20.000 kWh"),
    ]

    consumer_type = models.CharField(
        "Tipo de Consumidor", max_length=20, choices=consumer_type_choices
    )
    consumption_range = models.CharField(
        "Intervalo de Consumo", max_length=20, choices=consumption_range_choices
    )
    cover_value = models.FloatField("Valor de Cobertura")
    discount_value = models.FloatField("Valor de Desconto")

    def apply_discount(self, consumer):
        if (
            self.consumer_type == consumer.consumer_type
            and self.consumption_range == consumer.consumption_range
        ):
            return consumer.cover_value * (self.discount_value / 100)
        else:
            return 0


# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule


class Consumer(models.Model):
    name = models.CharField("Nome", max_length=128)
    document = models.CharField("Documento (CPF/CNPJ)", max_length=14, unique=True)
    city = models.CharField("Cidade", max_length=100)
    state = models.CharField("Estado", max_length=50)
    consumption = models.IntegerField("Consumo (kWh)")
    consumer_type = models.CharField("Tipo", max_length=20)
    cover_value = models.FloatField("Cobertura (%)")
    distributor_tax = models.FloatField("Tarifa da Distribuidora")

    discount_rule = models.ForeignKey(
        DiscountRule,
        on_delete=models.CASCADE,
        verbose_name="Regra de Desconto",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
