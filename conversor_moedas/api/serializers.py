from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from conversor_moedas.models import Conversao


class ConversaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversao
        fields = '__all__'

class ConversaoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Conversao
        fields = '__all__'