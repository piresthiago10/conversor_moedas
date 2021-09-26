from django.db import models
from django.db.models import fields
from rest_framework import serializers
from conversor_moedas.models import Conversao

class ConversaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversao
        fields = '__all__'