from django.contrib import admin

# Register your models here.
from sistema.models import Lanche, Pedido

admin.site.register(Lanche)
admin.site.register(Pedido)