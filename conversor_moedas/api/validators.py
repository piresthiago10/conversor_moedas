from rest_framework import serializers


class Validation() :

    def __init__(self, data: dict):
        self.data = data

    def validate(self) -> dict:
        if not self.valor_float(self.data['valor_conversao']):
            raise serializers.ValidationError(
                {"valor_conversao": "O valor precisa ser no formato de moeda. Ex: 15.00"})
        if not self.valor_positivo(self.data['valor_conversao']):
            raise serializers.ValidationError(
                {"valor_conversao": "O valor precisa ser maior que zero. Ex: 170.00"})
        if not self.moeda_permitida(self.data['moeda_origem']):
            raise serializers.ValidationError(
                {"moeda_origem": "Tipo de moeda não suportada pela aplicação."})
        if not self.moeda_permitida(self.data['moeda_final']):
            raise serializers.ValidationError(
                {"moeda_final": "Tipo de moeda não suportada pela aplicação."})
        return self.data

    def valor_float(self, valor: float) -> bool:
        """ Verifica se o valor inserido é do tipo float
        Ex: 15.00, 0.4578659, 4.00 """
        return isinstance(valor, float)

    def valor_positivo(self, valor: float) -> bool:
        """ Verifica se o valor é maior do que zero,
        ou seja, um valor positivo """
        return valor > 0

    def moeda_permitida(self, moeda: str) -> bool:
        """ Verifica se a moeda consta na lista de 
        correções monetárias permitidas """

        moedas = ['USD', 'BRL', 'EUR', 'BTC', 'ETH']

        return moeda.upper() in moedas