# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-02 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparks', '0017_auto_20170619_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spark',
            name='interests',
            field=models.CharField(choices=[('All', 'All'), ('Malnutrition', 'Malnutrition'), ('Education', 'Education'), ('Poverty', 'Poverty'), ('Social Welfare', 'Social Welfare'), ('Hygiene and Sanitation', 'Hygiene and Sanitation')], default='All', max_length=30),
        ),
    ]