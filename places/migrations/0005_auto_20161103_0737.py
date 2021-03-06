# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20161103_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='landscapeimg',
            name='description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='landscapeimg',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/landscape'),
        ),
        migrations.AddField(
            model_name='landscapeimg',
            name='landscape',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Landscape'),
        ),
        migrations.AddField(
            model_name='trail',
            name='description',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='trail',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='trail',
            name='longitue',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='trail',
            name='name',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='trail',
            name='subtitle',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='trailimg',
            name='description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='trailimg',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/trails'),
        ),
        migrations.AddField(
            model_name='trailimg',
            name='trail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Trail'),
        ),
    ]
