from rest_framework import serializers
from . import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = ['id', 'nome']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = ['id', 'preco', 'titulo']
    

class VendaSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(
        queryset=models.Produto.objects.all(),  
        write_only=True  
    )
    produto_nome = serializers.StringRelatedField(
        source = 'produto',
        read_only=True
    )
    class Meta:
        model = models.Venda
        fields = ['id', 'cliente', 'produto', 'produto_nome']

    