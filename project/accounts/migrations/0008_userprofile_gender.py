# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-10 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_user_interests'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('N', 'None'), ('M', 'Male'), ('F', 'Female')], default='N', max_length=1),
        ),
    ]
