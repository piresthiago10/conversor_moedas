from rest_framework import status
from conversor_moedas.models import Conversao
from rest_framework.test import APITestCase, APIRequestFactory


class ConversaoMoedasTestCase(APITestCase):

    def test_converte_moeda(self):
        response = self.client.get('?from=BTC&to=EUR&amount=123.45')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_amount_nao_float(self):
        response = self.client.get('?from=BTC&to=EUR&amount=a78')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valor_menor_zero(self):
        response = self.client.get('?from=BTC&to=EUR&amount=-784')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_moeda_nao_existente(self):
        response = self.client.get('?from=PHP&to=EUR&amount=30')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_parametro_errado(self):
        response = self.client.get('?fromm=USD&to=EUR&amount=30')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)