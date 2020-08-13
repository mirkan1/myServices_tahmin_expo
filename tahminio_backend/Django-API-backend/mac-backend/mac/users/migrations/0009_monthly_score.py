# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-06 09:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180616_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_point', models.PositiveIntegerField(default=0)),
                ('month', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
