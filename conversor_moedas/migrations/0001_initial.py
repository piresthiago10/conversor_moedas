# Generated by Django 3.2.7 on 2021-09-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moeda_origem', models.CharField(choices=[('USD', 'Dollar'), ('BRL', 'Real'), ('EUR', 'Euro'), ('BTC', 'Bitcoin'), ('ETH', 'Ethereum')], default='USD', max_length=3)),
                ('moeda_final', models.CharField(choices=[('USD', 'Dollar'), ('BRL', 'Real'), ('EUR', 'Euro'), ('BTC', 'Bitcoin'), ('ETH', 'Ethereum')], default='BRL', max_length=3)),
                ('valor_conversao', models.FloatField()),
                ('valor_convertido', models.FloatField(blank=True)),
                ('data_hora', models.DateField(blank=True)),
            ],
        ),
    ]
