import datetime
from datetime import date

from django.db import models

# Create your models here.
from django import forms


class Caixa(models.Model):
    STATUS = (
        ("ABERTO", "Aberto"),
        ("FECHADO", "fechado")
    )

    data_abertura = models.DateField(datetime.now())
    data_fechamento = models.DateField(null=True, verbose_name="Data de Fechamento")
    observacao = models.CharField(max_length=50, verbose_name="Observação")
    status = models.CharField(max_length=10, choices=STATUS, default="ABERTO")

    def __str__(self):
        return str(self.data_abertura)



class Ingrediente(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nome)


class Lanche(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    ingrediente = models.ManyToManyField(Ingrediente, blank=True)

    def __str__(self):
        return self.nome


class Bebida(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.nome


class Adicional(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS = (
        ("ATIVO", 'ativo'),
        ("CANCELADO", "cancelado"),
        ("BAIXADO", "baixado")

    )
    numero_pedido = models.CharField(max_length=5, unique=True)
    lanche = models.ManyToManyField(Lanche, blank=True)
    bebida = models.ManyToManyField(Bebida, blank=True)
    adicional = models.ManyToManyField(Adicional, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default="ATIVO")
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numero_pedido)



class Lancamento(models.Model):
    observacao = models.CharField(max_length=50, verbose_name="Observação")
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)

    def __str__(self):
        return self.observacao
