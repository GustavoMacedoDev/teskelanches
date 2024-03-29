from django.db import connection
from django.db.models import Sum
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404

from sistema.forms import CaixaForm
from sistema.models import *

# Create your views here.


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['numero_pedido', 'lanche', 'bebida', 'adicional', 'caixa']


class LancheForm(ModelForm):
    class Meta:
        model = Lanche
        fields = ['nome', 'valor', 'ingrediente']


class BebidaForm(ModelForm):
    class Meta:
        model = Bebida
        fields = ['nome', 'valor']


class IngredienteForm(ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome']


class LancamentoForm(ModelForm):
    class Meta:
        model = Lancamento
        fields = ['observacao', 'pedido', 'operacao']


def index(request, template_name='home/index.html'):
    return render(request, template_name)


def home(request, template_name='home/home.html'):
    return render(request, template_name)


def lista_lanches(request, template_name='lanche/lista_lanches.html'):
    lanche = Lanche.objects.all()
    lanches = {'lanche': lanche}
    return render(request, template_name, lanches)


def lanche_new(request, template_name='lanche/lanche_form.html'):
    form = LancheForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_lanches')
    return render(request, template_name, {'form': form })


def lanche_edit(request, pk, template_name='lanche/lanche_form.html'):
    lanche = get_object_or_404(Lanche, pk=pk)
    if request.method == "POST":
        form = LancheForm(request.POST, instance=lanche)
        if form.is_valid():
            lanche = form.save()
            return redirect('lista_lanches')
    else:
        form = LancheForm(instance=lanche)
    return render(request, template_name, {'form': form})


def lanche_delete(request, pk, template_name='lanche/lanche_delete.html'):
    lanche = Lanche.objects.get(pk=pk)
    if request.method == "POST":
        lanche.delete()
        return redirect('lista_lanches')
    return render(request, template_name, {'lanche': lanche})


def lista_bebidas(request, template_name='bebida/lista_bebidas.html'):
    bebida = Bebida.objects.all()
    bebidas = {'bebida': bebida}
    return render(request, template_name, bebidas)


def bebida_new(request, template_name='bebida/bebida_form.html'):
    form = BebidaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_bebidas')
    return render(request, template_name, {'form': form})


def bebida_edit(request, pk, template_name='bebida/bebida_form.html'):
    bebida = get_object_or_404(Bebida, pk=pk)
    if request.method == "POST":
        form = BebidaForm(request.POST, instance=bebida)
        if form.is_valid():
            form.save()
            return redirect('lista_bebidas')
    else:
        form = BebidaForm(instance=bebida)
    return render(request, template_name, {'form': form})


def lista_ingredientes(request, template_name='ingrediente/lista_ingredientes.html'):
    ingrediente = Ingrediente.objects.all()
    ingredientes = {'ingrediente': ingrediente}
    return render(request, template_name, ingredientes)


def ingrediente_new(request, template_name='ingrediente/ingrediente_form.html'):
    form = IngredienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_ingredientes')
    return render(request, template_name, {'form': form})


def ingrediente_edit(request, pk, template_name='ingrediente/ingrediente_form.html'):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    if request.method == "POST":
        form = IngredienteForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
            return redirect('lista_ingredientes')
    else:
        form = IngredienteForm(instance=ingrediente)
    return render(request, template_name, {'form': form})


#Pessoa#
#def listar_pessoas(request, template_name='pessoa/lista_pessoas.html'):
  #  pessoa = Pessoa.objects.all()
   # pessoas = {'pessoa': pessoa}
  #  return render(request, template_name, pessoas)


#def pessoa_new(request, template_name='pessoa/pessoa_form.html'):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pessoas')
    return render(request, template_name, {'form': form})


#def pessoa_edit(request, pk, template_name='pessoa/pessoa_form.html'):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa = form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, template_name, {'form': form})


#def pessoa_delete(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == "POST":
        pessoa.delete()
        return redirect('listar_pessoas')
    return render(request, 'pessoa_delete.html', {'pessoa': pessoa})


#Pedidos
def listar_pedidos(request, template_name='pedido/lista_pedidos.html'):
    pedido = Pedido.objects.filter(status="ATIVO")
    pedidos = {'pedido': pedido}
    return render(request, template_name, pedidos)


def pedido_new(request, template_name='pedido/pedido_form.html'):
    caixa = Caixa.objects.filter(status="ABERTO")
    form = PedidoForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('listar_pedidos')
    return render(request, template_name, {'form': form})


def pedido_edit(request, pk, template_name='pedido/pedido_form.html'):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido = form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, template_name, {'form': form})


def pedido_delete(request, pk, template_name='pedido/pedido_delete.html'):
    pedido = Pedido.objects.get(pk=pk)
    if request.method == "POST":
        pedido.delete()
        return redirect('listar_pedidos')
    return render(request, template_name, {'pedido': pedido})


def lista_pedidos_lanche(request, pk, template_name='pedido/pedido_lanche_list.html'):
    lanches = Lanche.objects.filter(pedido=pk)
    totallanches = Lanche.objects.filter(pedido=pk).aggregate(Sum('valor'))
    bebidas = Bebida.objects.filter(pedido=pk)
    totalbebidas = Bebida.objects.filter(pedido=pk).aggregate(Sum('valor'))
    adicionais = Adicional.objects.filter(pedido=pk)
    totaladicionais = Adicional.objects.filter(pedido=pk).aggregate(Sum('valor'))
    pedido = get_object_or_404(Pedido, pk=pk)

    totalb = totalbebidas['valor__sum']
    totall = totallanches['valor__sum']
    totala = totaladicionais['valor__sum']

    total = totall + totalb + totala

    return render(request, template_name, {'lanches': lanches, 'bebidas': bebidas,
                                           'adicionais': adicionais, 'pedido': pedido,
                                           'totallanches': totallanches, 'totalbebidas': totalbebidas,
                                           'total': total, 'totaladicionais': totaladicionais})


def fechar_pedido(request, pk, template_name='pedido/fecha_pedido.html'):
    form = LancamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        altera_status_pedido(self=pk)
        return redirect('listar_pedidos')
    return render(request, template_name, {'form': form})


def altera_status_pedido(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE sistema_pedido set STATUS = 'BAIXADO' WHERE id = %s", [self])
        #row = cursor.fetchone()

    #return row


def caixa_new(request, template_name='caixa/caixa_form.html'):
    form = CaixaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pedidos')
    return render(request, template_name, {'form': form})


def lista_caixa(request, template_name='caixa/lista_caixa.html'):
    caixa = Caixa.objects.filter(status="ABERTO")
    caixas = {'caixa': caixa}
    return render(request, template_name, caixas)


def lancamento_new(request, template_name='lancamento/lancamento_form.html'):
    form = LancamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pedidos')
    return render(request, template_name, {'form': form})


def relatorio_vendas(request, template_name='vendas/vendas.html'):
    vendas = Pedido.objects.all
