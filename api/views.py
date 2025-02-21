
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from . import serializers, models
from rest_framework.pagination import PageNumberPagination

class ClientesPagination(PageNumberPagination):
    page_size = 3
class ProdutosPagination(PageNumberPagination):
    page_size = 3
class VendasPagination(PageNumberPagination):
    page_size = 3

class ClienteViewSet(ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    http_method_names = ['get','post', 'patch', 'delete']
    pagination_class = ClientesPagination

class ProdutoViewSet(ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    pagination_class = ProdutosPagination

class VendaViewSet(ModelViewSet):
    queryset = models.Venda.objects.all()
    serializer_class = serializers.VendaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    pagination_class = VendasPagination


