# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-26 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_currency_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='code',
            field=models.CharField(blank=True, max_length=6, verbose_name='Code'),
        ),
    ]
