# Generated by Django 3.0.8 on 2022-04-16 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_auto_20220416_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ended',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 11, 5, 22, 850329), null=True, verbose_name='date ended'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_started',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 11, 5, 22, 850329), null=True, verbose_name='date started'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='date_register',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 11, 5, 22, 850329), null=True, verbose_name='date register'),
        ),
    ]