from conversor_moedas.api.integrations.crypto_compare import CryptoCompareApi
from conversor_moedas.api.serializers import (ConversaoSerializer,
                                              ConversaoSerializerV2)
from conversor_moedas.api.validators import Validation
from conversor_moedas.models import Conversao
from django.http.response import Http404
from rest_framework import generics, status, viewsets


class ConversaoViewSet(viewsets.ModelViewSet):
    """ Exibe todos as conversões de moedas """

    def get_queryset(self):
        try:
            moeda_origem = self.request.query_params.get('from')
            moeda_final = self.request.query_params.get('to')
            valor_conversao = float(self.request.query_params.get('amount'))
        except TypeError:
            raise Http404('Parametro não encontrado')

        data = {
            "moeda_origem": moeda_origem,
            "moeda_final": moeda_final,
            "valor_conversao": valor_conversao,
        }

        validation = Validation(data)
        data = validation.validate()
        valor_convertido = self.converte_moedas(
            moeda_origem, moeda_final, valor_conversao)

        conversao = Conversao(
            moeda_origem=data['moeda_origem'],
            moeda_final=data['moeda_final'],
            valor_conversao=data['valor_conversao'],
            valor_convertido=valor_convertido,
        )

        conversao.save()

        queryset = Conversao.objects.filter(pk=conversao.pk)

        return queryset

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

        return valor_convertido

    queryset = Conversao.objects.all()
    serializer_class = ConversaoSerializer
    http_method_names = ['get']


class ListaConversoes(generics.ListAPIView):
    def get_queryset(self):
        queryset = Conversao.objects.all().order_by('-data_hora')
        return queryset
    serializer_class = ConversaoSerializerV2
    http_method_names = ['get']
