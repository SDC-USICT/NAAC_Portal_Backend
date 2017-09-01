# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professional_details', '0003_auto_20170825_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='academic_experience',
            field=models.IntegerField(verbose_name='Academic Experience'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='awarded',
            field=models.CharField(max_length=100, verbose_name='Phd Awarded'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee ID'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='industrial_exp',
            field=models.IntegerField(verbose_name='Industrial Experience'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='phds',
            field=models.CharField(max_length=100, verbose_name='Total Student'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='pursuing',
            field=models.CharField(max_length=100, verbose_name='Phd Pursuing'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='qualification_after',
            field=models.CharField(max_length=100, verbose_name='Qualification Added'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='qualification_before',
            field=models.CharField(max_length=100, verbose_name='Highest Qualification'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='submitted',
            field=models.CharField(max_length=100, verbose_name='Phd Submitted'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='year',
            field=models.IntegerField(verbose_name='Year'),
        ),
    ]
