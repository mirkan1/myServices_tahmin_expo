# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20180419_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='match',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forum.Match'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prediction',
            name='game',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='upvote',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='prediction',
            unique_together=set([]),
        ),
    ]
