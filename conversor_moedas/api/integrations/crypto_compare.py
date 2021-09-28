from core.settings import DEBUG
from decouple import config
import requests
from rest_framework import request


class CryptoCompareApi:

    CRYPTOCOMPARE_API_URL = config("CRYPTOCOMPARE_API_URL")
    CRYPTOCOMPARE_TOKEN = config("CRYPTOCOMPARE_TOKEN")

    def get_lastro(self):
        response = requests.get(
            f'{CryptoCompareApi.CRYPTOCOMPARE_API_URL}/data/price?fsym=usd&tsyms=brl,eur,btc,eth&api_key={CryptoCompareApi.CRYPTOCOMPARE_TOKEN}')

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return response.status_code