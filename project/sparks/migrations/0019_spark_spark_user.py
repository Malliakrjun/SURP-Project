# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_user_interests'),
        ('sparks', '0018_auto_20170702_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='spark',
            name='spark_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
    ]