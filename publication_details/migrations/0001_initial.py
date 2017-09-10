# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0005_auto_20170903_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Book Title')),
                ('isbn', models.CharField(max_length=100, verbose_name='ISBN')),
                ('year', models.IntegerField(verbose_name='Year')),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='BookChapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title of Book Chapter')),
                ('book_title_and_publisher', models.CharField(max_length=100, verbose_name='Book Title with Publisher')),
                ('page_no', models.CharField(max_length=100, verbose_name='Page No.')),
                ('isbn', models.CharField(max_length=100, verbose_name='ISBN No.')),
                ('indexing', models.CharField(max_length=100, verbose_name='Indexing')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('month', models.CharField(max_length=12, verbose_name='Month')),
            ],
            options={
                'db_table': 'book_chapters',
            },
        ),
        migrations.CreateModel(
            name='CoAuthors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'co_authors',
            },
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title of Paper')),
                ('name_and_publisher', models.CharField(max_length=100, verbose_name='Name & Publisher')),
                ('volume_no', models.CharField(max_length=100, verbose_name='Vol no')),
                ('issn_isbn', models.CharField(max_length=100, verbose_name='ISBN No.')),
                ('indexing', models.CharField(max_length=100, verbose_name='Indexing')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('month', models.CharField(max_length=12, verbose_name='Month')),
                ('international_national', models.CharField(max_length=100, verbose_name='International/National')),
                ('author', models.ManyToManyField(related_name='employee_conf_author', to='publication_details.CoAuthors', verbose_name='Co Authors')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_conf', to='employee.Employee', verbose_name='Employee ID')),
            ],
            options={
                'db_table': 'conference',
            },
        ),
        migrations.CreateModel(
            name='JournalPapers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title of Paper')),
                ('name_and_publisher', models.CharField(max_length=100, verbose_name='Journal Name with Publisher')),
                ('volume_no', models.CharField(max_length=100, verbose_name='Vol. No.')),
                ('issn_isbn', models.CharField(max_length=100, verbose_name='ISSN No.')),
                ('indexing', models.CharField(max_length=100, verbose_name='Indexing')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('month', models.CharField(max_length=12, verbose_name='Month')),
                ('author', models.ManyToManyField(related_name='employee_jp_author', to='publication_details.CoAuthors', verbose_name='Co Authors')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_jp', to='employee.Employee', verbose_name='Employee ID')),
            ],
            options={
                'db_table': 'journal_papers',
            },
        ),
        migrations.AddField(
            model_name='bookchapters',
            name='author',
            field=models.ManyToManyField(related_name='employee_bc_author', to='publication_details.CoAuthors', verbose_name='Co Authors'),
        ),
        migrations.AddField(
            model_name='bookchapters',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_book_chapter', to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='employee_book_author', to='publication_details.CoAuthors', verbose_name='Co Authors'),
        ),
        migrations.AddField(
            model_name='book',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_book', to='employee.Employee', verbose_name='Employee ID'),
        ),
    ]
