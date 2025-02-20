from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    titulo = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.titulo

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.cliente.nome} comprou {self.produto.titulo}'

