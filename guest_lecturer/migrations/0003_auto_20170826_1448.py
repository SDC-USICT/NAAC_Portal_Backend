# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_lecturer', '0002_auto_20170825_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guestlecturer',
            old_name='insitute',
            new_name='institute',
        ),
    ]
