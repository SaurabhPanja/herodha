# Generated by Django 2.2.6 on 2019-10-18 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_trading', '0002_buytransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='funds',
            field=models.FloatField(default=100000.0),
        ),
    ]
