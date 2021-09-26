from rest_framework import viewsets
from conversor_moedas.api import serializers
from conversor_moedas.models import Conversao
from conversor_moedas.api.serializers import ConversaoSerializer

class ConversaoViewSet(viewsets.ModelViewSet):
    """ Exibe todos as conversões de moedas """
    queryset = Conversao.objects.all()
    serializer_class = ConversaoSerializer
    http_method_names = ['get', 'post']