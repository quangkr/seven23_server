# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 14:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('create', models.DateField(auto_now=True, verbose_name='Creation date')),
                ('archived', models.BooleanField(default=False, verbose_name='Is archived')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='currency.Currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user', 'create', 'name'),
                'verbose_name': 'Account',
            },
        ),
        migrations.CreateModel(
            name='InvitationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('create', models.DateField(auto_now=True, verbose_name='Creation date')),
            ],
            options={
                'ordering': ('create', 'email'),
                'verbose_name': 'Invitation Email',
            },
        ),
    ]