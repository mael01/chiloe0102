# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-17 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0024_auto_20170210_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beachimg',
            name='description_en_us',
        ),
        migrations.RemoveField(
            model_name='beachimg',
            name='description_es',
        ),
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='city',
            name='description_en_us',
            field=models.CharField(default='', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='description_es',
            field=models.CharField(default='', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='city',
            name='subtitle_en_us',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='subtitle_es',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cottage',
            name='description_en_us',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='cottage',
            name='description_es',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='cottage',
            name='subtitle_en_us',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cottage',
            name='subtitle_es',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='country',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hospital',
            name='description_en_us',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='description_es',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='subtitle_en_us',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='subtitle_es',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_en_us',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_es',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='subtitle_en_us',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='subtitle_es',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='landscape',
            name='description_en_us',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='landscape',
            name='description_es',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='landscape',
            name='subtitle_en_us',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='landscape',
            name='subtitle_es',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='description_en_us',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='description_es',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='subtitle_en_us',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='subtitle_es',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rentcar',
            name='description_en_us',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='rentcar',
            name='description_es',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='rentcar',
            name='subtitle_en_us',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rentcar',
            name='subtitle_es',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='description_en_us',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='description_es',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='subtitle_en_us',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='subtitle_es',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trail',
            name='description_en_us',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='trail',
            name='description_es',
            field=models.CharField(default='', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='trail',
            name='subtitle_en_us',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='trail',
            name='subtitle_es',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
