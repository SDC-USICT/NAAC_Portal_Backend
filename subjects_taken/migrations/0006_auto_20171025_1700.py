# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects_taken', '0005_auto_20170903_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectstaken',
            name='year',
            field=models.CharField(max_length=4, verbose_name=b'Year'),
        ),
    ]
