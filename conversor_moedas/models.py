from django.db import models
from django.db.models.expressions import F

class Conversao(models.Model):
   MOEDA = (
       ('USD', 'Dollar'),
       ('BRL', 'Real'),
       ('EUR', 'Euro'),
       ('BTC', 'Bitcoin'),
       ('ETH', 'Ethereum')
   )
   moeda_origem = models.CharField(max_length=3, choices=MOEDA, blank=False, default='USD')
   moeda_final = models.CharField(max_length=3, choices=MOEDA, blank=False, default='BRL')
   valor_conversao = models.FloatField(blank=False)
   valor_convertido = models.FloatField(blank=False)
   data_hora = models.DateTimeField(auto_now=True)

   def __str__(self) -> str:
       return self.moeda_origem + "-" + self.moeda_final
