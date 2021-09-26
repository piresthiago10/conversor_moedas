from django.db import models

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
   valor_conversao = models.FloatField()
   valor_convetido = models.FloatField()
   data_hora = models.DateField()

   def __str__(self) -> str:
       return self.moeda_origem + "-" + self.moeda_final
