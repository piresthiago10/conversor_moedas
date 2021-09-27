from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from conversor_moedas.models import Conversao
from conversor_moedas.api.validators import *


class ConversaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversao
        fields = ['id', 'moeda_origem', 'moeda_final', 'valor_conversao']

    def validate(self, data: dict) -> ValidationError:
        if not valor_float(data['valor_conversao']):
            raise serializers.ValidationError(
                {"valor_conversao": "O valor precisa ser no formato de moeda. Ex: 15.00"})
        if not valor_positivo(data['valor_conversao']):
            raise serializers.ValidationError(
                {"valor_conversao": "O valor precisa ser maior que zero. Ex: 170.00"})
        if not moeda_permitida(data['moeda_origem']):
            raise serializers.ValidationError(
                {"moeda_origem": "Tipo de moeda não suportada pela aplicação."})
        if not moeda_permitida(data['moeda_final']):
            raise serializers.ValidationError(
                {"moeda_final": "Tipo de moeda não suportada pela aplicação."})
        return data

class ConversaoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Conversao
        fields = '__all__'