# Generated by Django 3.2.7 on 2021-09-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversor_moedas', '0002_rename_valor_convetido_conversao_valor_convertido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversao',
            name='data_hora',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='conversao',
            name='valor_convertido',
            field=models.FloatField(blank=True),
        ),
    ]
