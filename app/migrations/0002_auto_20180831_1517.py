# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-31 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='line_val',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='game',
            name='ou_val',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
    ]
