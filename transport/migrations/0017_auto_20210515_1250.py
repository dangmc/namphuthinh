# Generated by Django 3.0.8 on 2021-05-15 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0016_auto_20210515_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ended',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 15, 12, 50, 46, 502123), null=True, verbose_name='date ended'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_started',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 15, 12, 50, 46, 502123), null=True, verbose_name='date started'),
        ),
    ]
