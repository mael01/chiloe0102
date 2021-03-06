# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 07:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20161103_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='beachimg',
            name='datestore',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='beachimg',
            name='description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='beachimg',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/beachs'),
        ),
        migrations.AddField(
            model_name='beachimg',
            name='principal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='landscape',
            name='description',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='landscape',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='landscape',
            name='longitue',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='landscape',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='landscape',
            name='subtitle',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
