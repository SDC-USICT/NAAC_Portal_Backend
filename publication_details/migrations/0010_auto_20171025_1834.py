# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_details', '0009_auto_20171025_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(default=1900, verbose_name=b'ISBN'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.CharField(max_length=4, verbose_name=b'Year'),
        ),
        migrations.AlterField(
            model_name='bookchapters',
            name='isbn',
            field=models.IntegerField(verbose_name=b'ISBN No.'),
        ),
        migrations.AlterField(
            model_name='bookchapters',
            name='page_no',
            field=models.IntegerField(verbose_name=b'Page No.'),
        ),
        migrations.AlterField(
            model_name='bookchapters',
            name='year',
            field=models.CharField(max_length=4, verbose_name=b'Year'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='issn_isbn',
            field=models.IntegerField(verbose_name=b'ISBN No.'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='year',
            field=models.CharField(max_length=4, verbose_name=b'Year'),
        ),
    ]