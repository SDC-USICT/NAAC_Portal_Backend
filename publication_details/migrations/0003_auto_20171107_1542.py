# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_details', '0002_auto_20171105_0455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journalpapers',
            old_name='name_and_publisher',
            new_name='name',
        ),
        migrations.AddField(
            model_name='journalpapers',
            name='publisher',
            field=models.CharField(default=212, max_length=100, verbose_name=b'Journal Name with Publisher'),
            preserve_default=False,
        ),
    ]
