# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20161103_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='beach',
            name='description',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='beach',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='beach',
            name='longitue',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='beach',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='beach',
            name='subtitle',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
