def valor_float(valor: float) -> bool:
    """ Verifica se o valor inserido é do tipo float
    Ex: 15.00, 0.4578659, 4.00 """
    return isinstance(valor, float)

def valor_positivo(valor: float) -> bool:
    """ Verifica se o valor é maior do que zero,
    ou seja, um valor positivo """
    return valor > 0

def moeda_permitida(moeda: str) -> bool:
    """ Verifica se a moeda consta na lista de 
    correções monetárias permitidas """

    moedas = ['USD', 'BRL', 'EUR', 'BTC', 'ETH']

    return moeda.upper() in moedas