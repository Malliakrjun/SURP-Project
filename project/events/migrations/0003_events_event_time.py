# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-18 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_events_incomplete'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_time',
            field=models.DateTimeField(null=True),
        ),
    ]
