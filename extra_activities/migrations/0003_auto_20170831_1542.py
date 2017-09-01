# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extra_activities', '0002_auto_20170825_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='department',
            field=models.CharField(max_length=100, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='extra',
            name='details',
            field=models.CharField(max_length=100, verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='extra',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee ID'),
        ),
        migrations.AlterField(
            model_name='extra',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='extra',
            name='year',
            field=models.IntegerField(verbose_name='Year'),
        ),
    ]
