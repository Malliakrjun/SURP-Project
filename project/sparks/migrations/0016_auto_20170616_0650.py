# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-16 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparks', '0015_auto_20170609_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spark',
            name='image',
            field=models.ImageField(blank=True, upload_to='sparks'),
        ),
    ]