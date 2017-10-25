# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patents', '0005_auto_20170903_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='patents',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='patents',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Patent Type'),
        ),
    ]
