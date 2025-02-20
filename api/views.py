from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from . import serializers, models

class ClientesView(ListCreateAPIView):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer


