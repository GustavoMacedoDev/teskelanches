from django.db import models

# Create your models here.
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#from sistema.serializers import LancheSerializer


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



#APi


#class LancheList(APIView):
    def pos(self, request):
        try:
            serializer = LancheSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)