from django.db import models

# Create your models here.
from employee.models import Employee


class JournalPapers(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_jp', verbose_name='Employee ID')
    title = models.CharField("Title of Paper",max_length=100, blank=True, null=True)
    name_and_publisher = models.CharField("Journal Name with Publisher",max_length=100)
    volume_no = models.CharField("Vol. No.",max_length=100)
    issn_isbn = models.IntegerField("ISSN No.")
    indexing = models.CharField("Indexing",max_length=100)
    month = models.CharField("Month",max_length=12)
    hindex = models.CharField("H-Index of Journal using Scimago (if Scopus, SCI-Ex or SCI)", max_length=100, blank=True, null=True)
    impact_factor = models.CharField("Impact Factor if SCI-Ex or SCI", max_length=100, blank=True, null=True)
    coauthor = models.TextField(max_length=200, verbose_name='Co Authors', blank=True,null=True)

    class Meta:
        db_table = 'journal_papers'


class Conference(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_conf', verbose_name='Employee ID')
    title = models.CharField("Title of Paper",max_length=100, blank=True, null=True)
    name_and_publisher = models.CharField('Name & Publisher', max_length=100)
    issue_no = models.CharField('Issue no', max_length=100, null=True, blank=True)
    issn_isbn = models.IntegerField("ISBN No.")
    indexing = models.CharField("Indexing",max_length=100)
    year = models.CharField("Year",max_length=4)
    international_national = models.CharField("International/National",max_length=100)
    coauthor = models.TextField(max_length=200, verbose_name='Co Authors',blank=True,null=True)
    page_no_start = models.CharField('Page number starting', max_length=100, blank=True, null=True)
    page_no_end =  models.CharField('Page number ending', max_length=100, blank=True, null=True)


    class Meta:
        db_table = 'conference'


class BookChapters(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_book_chapter')
    title = models.CharField("Title of Book Chapter",max_length=100, blank=True,null=True)
    book_title_and_publisher = models.CharField("Book Title with Publisher",max_length=100)
    page_no = models.IntegerField("Page No.")
    isbn = models.IntegerField("ISBN No.")
    indexing = models.CharField("Indexing",max_length=100)
    year = models.CharField("Year",max_length=4)
    month = models.CharField("Month",max_length=12)
    coauthor = models.TextField(max_length=200, verbose_name='Co Authors',blank=True,null=True)


    class Meta:
        db_table = 'book_chapters'


class Book(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_book')
    title = models.CharField(max_length=100, verbose_name='Title of Book', blank=True, null=True)
    isbn = models.IntegerField('ISBN')
    year = models.CharField("Year",max_length=4)
    coauthor = models.TextField(max_length=200, verbose_name='Co Authors',blank=True,null=True)
    page_no_start = models.CharField('Page number starting', max_length=100, blank=True, null=True)
    page_no_end = models.CharField('Page number ending', max_length=100, blank=True, null=True)


class Meta:
        db_table = 'book'
