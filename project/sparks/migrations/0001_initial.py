# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spark_name', models.CharField(max_length=100)),
                ('spark_locality', models.CharField(default='', max_length=100)),
                ('spark_city', models.CharField(default='', max_length=100)),
                ('spark_mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
