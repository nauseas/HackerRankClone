# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problemas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(blank=True, max_length=255)),
                ('instrucciones', models.CharField(blank=True, max_length=255)),
                ('timestamp', models.DateField(auto_now=True)),
            ],
        ),
    ]
