# Generated by Django 4.2.17 on 2024-12-12 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_from', models.CharField(choices=[('USD', 'Dólar Estadounidense'), ('PEN', 'Nuevo Sol Peruano')], max_length=3)),
                ('currency_to', models.CharField(choices=[('USD', 'Dólar Estadounidense'), ('PEN', 'Nuevo Sol Peruano')], max_length=3)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
