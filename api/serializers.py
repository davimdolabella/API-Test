from rest_framework import serializers
from . import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = ['id', 'nome']