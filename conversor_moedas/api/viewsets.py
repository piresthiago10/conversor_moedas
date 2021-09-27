from rest_framework import status, viewsets, generics
from conversor_moedas.models import Conversao
from conversor_moedas.api.serializers import ConversaoSerializer, ConversaoSerializerV2
from rest_framework.response import Response
from datetime import datetime
from conversor_moedas.api.integrations.crypto_compare import CryptoCompareApi

class ConversaoViewSet(viewsets.ModelViewSet):
    """ Exibe todos as conversões de moedas """
    queryset = Conversao.objects.all()
    serializer_class = ConversaoSerializer
    http_method_names = ['get', 'post']

class ListaConversoes(generics.ListAPIView):
    def get_queryset(self):
        queryset = Conversao.objects.all().order_by('-data_hora')
        return queryset
    serializer_class = ConversaoSerializerV2

class ListaConversoesViewSet(viewsets.ModelViewSet):
    """ Exibe todos as conversões de moedas """
    queryset = Conversao.objects.all()
    serializer_class = ConversaoSerializerV2
    http_method_names = ['get', 'post']

    def get_valores_moedas(self):
        crypto_compare_api = CryptoCompareApi()
        lastro_dolar = crypto_compare_api.get_lastro()
        """ É possível implementar um loop para percorrer uma lista com
        as moedas aceitas pelos requisitos. """
        brl = lastro_dolar['BRL']
        eur = lastro_dolar['EUR']
        btc = lastro_dolar['BTC']
        eth = lastro_dolar['ETH']

        moedas = {"BRL": brl, "EUR": eur, "BTC": btc, "ETH": eth}

        return moedas

    def converte_moedas(self, moeda_origem, moeda_final, valor_conversao):
        moedas = self.get_valores_moedas()
        if moeda_origem == "USD":
            valor_moeda_origem = 1.0
        else:
            valor_moeda_origem = moedas.get(moeda_origem)
        if moeda_final == "USD":
            valor_moeda_final = 1.0
        else:
            valor_moeda_final = moedas.get(moeda_final)
        conversao_moeda = (1.00 / valor_moeda_origem) * valor_moeda_final
        valor_convertido = conversao_moeda * valor_conversao

        dados_conversao = {
            "moeda_origem": moeda_origem,
            "moeda_final": moeda_final,
            "valor_conversao": valor_conversao,
            "valor_convertido": valor_convertido,
            "data_hora": datetime.now()
        }

        return dados_conversao

    def create(self, request, moeda_origem, moeda_final, valor_conversao):
        moeda_origem = moeda_origem
        moeda_final = moeda_final
        valor_conversao = valor_conversao
        dados_conversao = self.converte_moedas(moeda_origem, moeda_final, valor_conversao)
        serializer = self.serializer_class(data=dados_conversao)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            return response

