# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-29 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20161229_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beachimg',
            name='beach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beach_imgs', to='places.Beach'),
        ),
        migrations.AlterField(
            model_name='landscapeimg',
            name='landscape',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='landscape_imgs', to='places.Landscape'),
        ),
        migrations.AlterField(
            model_name='trailimg',
            name='trail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trail_imgs', to='places.Trail'),
        ),
        migrations.AlterUniqueTogether(
            name='beach',
            unique_together=set([('city',)]),
        ),
        migrations.AlterUniqueTogether(
            name='beachimg',
            unique_together=set([('beach',)]),
        ),
        migrations.AlterUniqueTogether(
            name='landscapeimg',
            unique_together=set([('landscape',)]),
        ),
        migrations.AlterUniqueTogether(
            name='trailimg',
            unique_together=set([('trail',)]),
        ),
    ]