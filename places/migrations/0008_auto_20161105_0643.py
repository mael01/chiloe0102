# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20161105_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='landscapeimg',
            name='principal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trailimg',
            name='principal',
            field=models.BooleanField(default=False),
        ),
    ]
