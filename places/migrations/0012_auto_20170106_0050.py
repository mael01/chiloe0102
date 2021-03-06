# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-06 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_auto_20170106_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='img_refer',
            field=models.ImageField(null=True, upload_to='static/img/hospital'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='img_refer',
            field=models.ImageField(null=True, upload_to='static/img/hotel'),
        ),
        migrations.AlterField(
            model_name='rentcar',
            name='img_refer',
            field=models.ImageField(null=True, upload_to='static/img/rentcar'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='img_refer',
            field=models.ImageField(null=True, upload_to='static/img/restaurant'),
        ),
    ]
