# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_merge_20170901_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='employee_id',
            new_name='employee',
        ),
    ]
