# Generated by Django 3.2.7 on 2021-09-27 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversor_moedas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversao',
            name='data_hora',
            field=models.DateTimeField(),
        ),
    ]
