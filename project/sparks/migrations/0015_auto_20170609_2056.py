# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparks', '0014_auto_20170609_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spark',
            name='image',
            field=models.ImageField(blank=True, default='accounts/m-user.png', upload_to='sparks'),
        ),
    ]
