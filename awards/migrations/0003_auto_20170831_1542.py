# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20170825_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_awards', to='employee.Employee', verbose_name='Employee ID'),
        ),
        migrations.AlterField(
            model_name='awards',
            name='month',
            field=models.CharField(max_length=100, verbose_name='Month'),
        ),
        migrations.AlterField(
            model_name='awards',
            name='organisation',
            field=models.CharField(max_length=100, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='awards',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='awards',
            name='year',
            field=models.IntegerField(verbose_name='Year'),
        ),
    ]
