# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-16 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170616_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
