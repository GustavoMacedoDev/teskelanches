from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/index', index),
#    url(r'^pessoa/lista_pessoas/', listar_pessoas, name='listar_pessoas'),
 #   url(r'^pessoa/pessoa_new/', pessoa_new, name='pessoa_new'),
  #  url(r'^pessoa/pessoa_edit/(?P<pk>[0-9]+)', pessoa_edit, name='pessoa_edit'),
   # url(r'^pessoa/pessoa_delete/(?P<pk>[0-9]+)', pessoa_delete, name='pessoa_delete'),


    url(r'^pedido/lista_pedidos/', listar_pedidos, name='listar_pedidos'),
    url(r'^pedido/pedido_new/', pedido_new, name='pedido_new'),
    url(r'^pedido/pedido_edit/(?P<pk>[0-9]+)', pedido_edit, name='pedido_edit'),
    url(r'^pedido/pedido_delete/(?P<pk>[0-9]+)', pedido_delete, name='pedido_delete'),
    url(r'^pedido/lanche/(?P<pk>[0-9]+)', lista_pedidos_lanche, name='lista_pedidos_lanche')

]