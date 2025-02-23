
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from . import serializers, models
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

class ListPagination(PageNumberPagination):
    page_size = 3

class ApiBaseViewSet(ModelViewSet):
    http_method_names = ['get','post', 'patch', 'delete']
    pagination_class = ListPagination
    permission_classes = [IsAuthenticated,]

class ClienteViewSet(ApiBaseViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    

class ProdutoViewSet(ApiBaseViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer

class VendaViewSet(ApiBaseViewSet):
    queryset = models.Venda.objects.all()
    serializer_class = serializers.VendaSerializer


