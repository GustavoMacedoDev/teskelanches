from django.db import models

# Create your models here.


class Lanche(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=20, decimal_places=2)

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
    numero_pedido = models.CharField(max_length=5, unique=True)
    lanche = models.ManyToManyField(Lanche, blank=True)
    bebida = models.ManyToManyField(Bebida, blank=True)
    adicional = models.ManyToManyField(Adicional, blank=True)

    def __str__(self):
        return str(self.numero_pedido)

