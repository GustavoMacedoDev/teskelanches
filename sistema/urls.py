from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/index', index, name='index'),
    url(r'^home/home', home, name='nome'),
#    url(r'^pessoa/lista_pessoas/', listar_pessoas, name='listar_pessoas'),
 #   url(r'^pessoa/pessoa_new/', pessoa_new, name='pessoa_new'),
  #  url(r'^pessoa/pessoa_edit/(?P<pk>[0-9]+)', pessoa_edit, name='pessoa_edit'),
   # url(r'^pessoa/pessoa_delete/(?P<pk>[0-9]+)', pessoa_delete, name='pessoa_delete'),


    url(r'^pedido/lista_pedidos/', listar_pedidos, name='listar_pedidos'),
    url(r'^pedido/pedido_new/', pedido_new, name='pedido_new'),
    url(r'^pedido/pedido_edit/(?P<pk>[0-9]+)', pedido_edit, name='pedido_edit'),
    url(r'^pedido/pedido_delete/(?P<pk>[0-9]+)', pedido_delete, name='pedido_delete'),
    url(r'^pedido/lanche/(?P<pk>[0-9]+)', lista_pedidos_lanche, name='lista_pedidos_lanche'),

    url(r'^lanche/lista_lanches', lista_lanches, name='lista_lanches'),
    url(r'^lanche/lanche_new', lanche_new, name='lanche_new'),
    url(r'^lanche/lanche_edit/(?P<pk>[0-9]+)', lanche_edit, name='lanche_edit'),
    url(r'^lanche/lanche_delete/(?P<pk>[0-9]+)', lanche_delete, name='lanche_delete'),

    url(r'^bebida/lista_bebidas', lista_bebidas, name='lista_bebidas'),
    url(r'^bebida/bebida_new', bebida_new, name='bebida_new'),
    url(r'^bebida/bebida_edit/(?P<pk>[0-9]+)', bebida_edit, name='bebida_edit'),


    url(r'^ingrediente/lista_ingrediente', lista_ingredientes, name='lista_ingredientes'),
    url(r'^ingrediente/ingrediente_new', ingrediente_new, name='ingrediente_new'),
    url(r'^ingrediente/ingrediente_edit/(?P<pk>[0-9]+)', ingrediente_edit, name='ingrediente_edit'),


    url(r'^caixa/caixa_new', caixa_new, name='caixa_new'),


    url(r'^lancamento/lancamento_new', lancamento_new, name='lancamento_new')

]