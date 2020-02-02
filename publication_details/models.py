from django.db import models

# Create your models here.
from employee.models import Employee


class JournalPapers(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_jp', verbose_name='Employee ID', on_delete=models.PROTECT)
    title = models.CharField("Title of Paper",max_length=100, blank=True, null=True)
    name = models.CharField("Journal Name with Publisher",max_length=100)
    publisher = models.CharField("Journal Name with Publisher",max_length=100)
    volume_no = models.CharField("Vol. No.",max_length=100)
    issn_isbn = models.IntegerField("ISSN No.")
    indexing = models.CharField("Indexing",max_length=100)
    month = models.CharField("Month",max_length=12)
    hindex = models.IntegerField("H-Index of Journal using Scimago (if Scopus, SCI-Ex or SCI)",blank=True,null=True)
    impact_factor = models.IntegerField("Impact Factor if SCI-Ex or SCI",blank=True,null=True)
    coauthor = models.TextField(max_length=200, verbose_name='Co Authors', blank=True,null=True)
    ugcCheck = models.BooleanField(default=False)
    year = models.IntegerField("Year",blank=True, null=True)
    page_no_start = models.IntegerField('Page number starting',blank=True, null=True)
    page_no_end =  models.IntegerField('Page number ending',blank=True, null=True)
    citation = models.IntegerField(blank=True, null=True)
    numcitations = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'journal_papers'


class Conference(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_conf', verbose_name='Employee ID', on_delete=models.PROTECT)
    title = models.CharField("Title of Paper",max_length=100, blank=True, null=True)
    name_and_publisher = models.CharField('Name & Publisher', max_length=100)
    issue_no = models.IntegerField('Issue no')
    issn_isbn = models.IntegerField("ISBN No.")
    indexing = models.CharField("Indexing",max_length=100)
    year = models.CharField("Year",max_length=4)
    international_national = models.CharField("International/National",max_length=100)
    coauthor = models.TextField(max_length=200, verbose_name='Co Authors',blank=True,null=True)
    page_no_start = models.IntegerField('Page number starting')
    page_no_end =  models.IntegerField('Page number ending')
    month = models.CharField("Month",max_length=12,blank=True, null=True)
    role = models.CharField("Role",max_length=30,blank=True, null=True)
    Institutional_Affiliation = models.CharField("Institutional Affiliation As Mentioned",blank=True,null=True,max_length=100)


    class Meta:
        db_table = 'conference'


class BookChapters(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_book_chapter', on_delete=models.PROTECT)
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
    employee = models.ForeignKey(Employee, related_name='employee_book', on_delete=models.PROTECT)
    title = models.CharField(max_length=100, verbose_name='Title of Book', blank=True, null=True)
    isbn = models.IntegerField('ISBN')
    year = models.CharField("Year",max_length=4)
    coauthor = models.TextField(max_length=200, verbose_name='Co Authors',blank=True,null=True)
    page_no_start = models.IntegerField('Page number starting')
    page_no_end = models.IntegerField('Page number ending')


class Meta:
        db_table = 'book'
