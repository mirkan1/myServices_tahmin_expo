# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20180418_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='iyscore',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='score',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
