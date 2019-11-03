from django.contrib import admin

# Register your models here.
from sistema.models import Lanche, Pedido, Bebida, Ingrediente

admin.site.register(Lanche)
admin.site.register(Pedido)
admin.site.register(Bebida)
admin.site.register(Ingrediente)