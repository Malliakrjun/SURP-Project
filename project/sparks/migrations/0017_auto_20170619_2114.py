# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparks', '0016_auto_20170616_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spark',
            name='interests',
            field=models.CharField(choices=[('All', 'All'), ('Malnutrition', 'Malnutrition'), ('Education', 'Education'), ('Poverty', 'Poverty'), ('Social Welfare', 'Social Welfare'), ('Hygiene and Sanitation', 'Hygiene and Sanitation')], default='All', max_length=25),
        ),
    ]