# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 05:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sparks', '0008_spark_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spark',
            old_name='spark_name',
            new_name='spark_full_name',
        ),
    ]
