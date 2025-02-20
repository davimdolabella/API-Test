from django.contrib import admin
from . import models

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    ...
@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    ...
@admin.register(models.Venda)
class VendaAdmin(admin.ModelAdmin):
    ordering = ['cliente__nome']

